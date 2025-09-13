# Фикстуры
import pytest
import requests
import auth_data as auth_data

# Базовый URL
@pytest.fixture(scope="session")
def base_url():
    return auth_data.URL

# Заголовки для авторизации
@pytest.fixture(scope="session")
def headers():
    return auth_data.HEADERS

# ID Тренера для тестов
@pytest.fixture(scope="session")
def trainer_id():
    return auth_data.Trainer_ID

# Клиент для работы с API
@pytest.fixture
def api_client(base_url, headers):
    class APIClient:
        def __init__(self, base_url, headers):
            self.base_url = base_url
            self.headers = headers
        
        def get(self, endpoint, **kwargs):
            return requests.get(f"{self.base_url}{endpoint}", headers=self.headers, **kwargs)
        
        def put(self, endpoint, **kwargs):
            return requests.put(f"{self.base_url}{endpoint}", headers=self.headers, **kwargs)
        
        def patch(self, endpoint, **kwargs):
            return requests.patch(f"{self.base_url}{endpoint}", headers=self.headers, **kwargs)
        
    return APIClient(base_url, headers)

# Восстановление данных после тестов
@pytest.fixture
def cleanup_trainer_data(api_client, trainer_id):
    # Сохранение оригинальных данных перед тестом
    original_response = api_client.get('/trainers', params={'trainer_id': trainer_id})
    original_data = original_response.json()["data"][0] if original_response.json()["data"] else {}

    yield  # Выполнение теста

    # Восстановление оригинальных данных после теста
    if original_data:
        restore_data = {
            "name": original_data.get("trainer_name", "Ash"),
            "city": original_data.get("city", "Pallet Town")
        }
        api_client.put('/trainers', json=restore_data)