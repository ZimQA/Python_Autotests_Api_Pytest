# Python API Autotests with Pytest | Автотесты на Python  
🐍 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 🐍
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-0A9EDC?logo=pytest&logoColor=white)
![API](https://img.shields.io/badge/API-REST%20Testing-FF6F61?logo=postman&logoColor=white)
![Automation](https://img.shields.io/badge/Automation-100%25-00CC00?logo=automation&logoColor=white)

🐍 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 🐍

## 🎯 Ключевые особенности

- ✅ **Полное покрытие API** - Тестирование всех основных эндпоинтов
- 🚀 **Высокая производительность** - Быстрые и эффективные тесты  
- 📊 **Параметризованное тестирование** - Множество сценариев в одном тесте
- 🏗 **Чистая архитектура** - Логичная структура проекта и кода
- 🔧 **Гибкая конфигурация** - Легкая настройка под разные среды
- 📝 **Детальная отчетность** - Понятные результаты тестирования
- 🛡 **Надежность** - Стабильные и предсказуемые тесты

## 🛠 Технологический стек

| Технология | Назначение | Версия |
|------------|------------|---------|
| **Python** | Основной язык программирования | 3.8+ |
| **Pytest** | Фреймворк для тестирования | 7.4+ |
| **Requests** | HTTP-клиент для API запросов | 2.31+ |
| **JSON** | Работа с данными и валидация | - |
| **Fixtures** | Управление состоянием тестов | - |
| **Parametrize** | Параметризованное тестирование | - |

🐍 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 🐍

## 📁 Структура проекта

```
Python_Autotest_Api_Pytest/
├── 📂 tests/                          # Папка с тестами
│   ├── 🐍 __init__.py                 # Инициализация пакета тестов
│   ├── ⚙️ conftest.py                 # Фикстуры и конфигурация Pytest
│   ├── 🧪 test_trainers.py            # Основные тесты API эндпоинтов
│   └── 📋 static_bodies.py            # Тестовые данные и тела запросов
├── 🔐 auth_data.py                    # Конфигурация API (токены, URL)
├── 📖 README.md                       # Документация проекта
└── 🗑️ .gitignore                      # Исключения для Git
```

### 📋 Описание файлов:
- **`conftest.py`** - Фикстуры Pytest для работы с API клиентом и данными
- **`test_trainers.py`** - Тесты для эндпоинтов /trainers (GET, PUT, PATCH)
- **`static_bodies.py`** - Тестовые данные для параметризованного тестирования
- **`auth_data.py`** - Настройки подключения к API (токен, URL, headers)
---
## 🎯 Примеры кода

### 🔧 Фикстура API клиента
```python
@pytest.fixture
def api_client(base_url, headers):
    class APIClient:
        def get(self, endpoint, **kwargs):
            return requests.get(f"{self.base_url}{endpoint}", headers=self.headers, **kwargs)
    return APIClient(base_url, headers)
```
### 📊 Параметризация эндпоинтов
```python
@pytest.mark.parametrize("endpoint", [
    "/trainers",
    "/trainers?limit=5", 
    "/trainers?page=1"
])
def test_status_code(api_client, endpoint):
    response = api_client.get(endpoint)
    assert response.status_code == 200
```
### 🎯 Параметризация данных тренера
```python
@pytest.mark.parametrize("test_id,expected_name", [
    (39589, "Ash")
])
def test_trainer_by_id(api_client, test_id, expected_name):
    response = api_client.get('/trainers', params={'trainer_id': test_id})
    trainer = response.json()["data"][0]
    assert trainer["trainer_name"] == expected_name
```
### 📋 Тестовые данные
```python
PUT_TEST_DATA = [
    {"name": "Ash", "city": "Tokyo"},
    {"name": "Ash Ketchum", "city": "Pallet Town"}
]

PATCH_TEST_DATA = [
    {"name": "Ash"},
    {"city": "Tokyo"}
]
```
### ⚡ Фикстура очистки данных
```python
@pytest.fixture
def cleanup_trainer_data(api_client, trainer_id):
    original_response = api_client.get('/trainers', params={'trainer_id': trainer_id})
    original_data = original_response.json()["data"][0]
    
    yield
    
    restore_data = {
        "name": original_data.get("trainer_name", "Ash"),
        "city": original_data.get("city", "Tokyo")
    }
    api_client.put('/trainers', json=restore_data)
```
---
## 🎉 Автор проекта

**Магия тестирования от ZimQA** ✨
**Happy testing! 🎯🐍🚀**
