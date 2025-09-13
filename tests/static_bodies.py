# Данные для параметризации PUT запросов (полное обновление)
PUT_TEST_DATA = [
    {"name": "Ash", "city": "Tokyo"},
    {"name": "Ash Ketchum", "city": "Pallet Town"},
    {"name": "Satoshi", "city": "Masara Town"},
    {"name": "Ash", "city": "Veridian City"}
]

# Данные для параметризации PATCH запросов (частичное обновление)
PATCH_TEST_DATA = [
    {"name": "Ash"},
    {"name": "Ash Ketchum"},
    {"name": "Red"},
    {"city": "Tokyo"},
    {"city": "Saffron City"},
    {"name": "Ash", "city": "Tokyo"}
]

# Тестовые ID тренеров
TRAINER_IDS_TO_TEST = [39589]

# Дефолтные значения для отката изменений
DEFAULT_TRAINER_DATA = {"name": "Ash", "city": "Tokyo"}