import pytest
import tests.static_bodies as static_bodies
from tests.conftest import api_client, cleanup_trainer_data, trainer_id

# GET/trainers - Статус код 200
@pytest.mark.parametrize("endpoint", [
    "/trainers",
    "/trainers?limit=5", 
    "/trainers?page=1"
])
def test_status_code(api_client, endpoint):
    response = api_client.get(endpoint)

    assert response.status_code == 200
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)  # data должен быть списком
    assert response.elapsed.total_seconds() < 2.0     # Проверка времени ответа
    assert "application/json" in response.headers["Content-Type"]  # Проверка Content-Type

# Проверка строчки с именем по id
@pytest.mark.parametrize("test_id, expected_name", [
    (39589, "Ash"),
])
def test_part_of_response(api_client, test_id, expected_name):
    response = api_client.get('/trainers', params={'trainer_id' : test_id})

    assert response.status_code == 200
    assert "data" in response.json()
    assert isinstance(response.json()["data"], list)
    
    # Если тренер найден
    if response.json()["data"]:
        assert len(response.json()["data"]) == 1  # Должен вернуть только одного
        trainer = response.json()["data"][0]
        assert trainer["trainer_name"] == expected_name
        assert isinstance(trainer["id"], (int, str))     # ID должен быть числом
        assert str(trainer["id"]) == str(test_id)  # ID должен совпадать
        assert "city" in trainer                  # Проверка наличия дополнительных полей

# PUT/trainers - Обновление информации
@pytest.mark.parametrize("update_data", static_bodies.PUT_TEST_DATA)
def test_put_trainers(api_client, trainer_id, cleanup_trainer_data, update_data):
    response = api_client.put('/trainers', json=update_data)
    assert response.status_code == 200

    # Проверка что данные действительно обновились
    get_response = api_client.get('/trainers', params={'trainer_id': trainer_id})
    updated_trainer = get_response.json()["data"][0]
    
    if "name" in update_data:
        assert updated_trainer["trainer_name"] == update_data["name"]
    if "city" in update_data:
        assert updated_trainer["city"] == update_data["city"]
    
# PATCH/trainers - Частичное обновление информации
@pytest.mark.parametrize("partial_data", static_bodies.PATCH_TEST_DATA)
def test_patch_trainers(api_client, partial_data, trainer_id, cleanup_trainer_data):
    response = api_client.patch('/trainers', json=partial_data)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    # Проверка частичного обновления
    get_response = api_client.get('/trainers', params={'trainer_id':trainer_id})
    updated_trainer = get_response.json()["data"][0]

    if "name" in partial_data:
        assert updated_trainer["trainer_name"] == partial_data["name"]
    if "city" in partial_data:
        assert updated_trainer["city"] == partial_data["city"]

# Проверка времени ответа сервера
@pytest.mark.parametrize("response_time_limit", [1.0, 2.0, 3.0])
def test_response_time_performance(api_client, response_time_limit):
    response = api_client.get('/trainers')
    assert response.elapsed.total_seconds() < response_time_limit

# Проверка всех обязательных полей
@pytest.mark.parametrize("required_field", [
    "id",
    "trainer_name",
    "level",
    "pokemons",
    "pokemons_alive",
    "pokemons_in_pokeballs",
    "get_history_battle",
    "is_premium",
    "premium_duration",
    "avatar_id",
    "city"
])
def test_response_contains_required_fields(api_client, trainer_id, required_field):
    response = api_client.get('/trainers', params={'trainer_id': trainer_id})
    trainer = response.json()["data"][0]
    assert required_field in trainer