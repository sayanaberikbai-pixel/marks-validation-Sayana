# Проверка баллов 0–100 (`marks.csv`)

Сквозной проект: валидация колонки `points` — значения от **0 до 100**, без `NaN`.

## Структура проекта
marks-validation/
├── marks.csv          # Исходный файл с данными
├── marks_clean.csv    # Только валидные строки (результат задачи 12)
├── marks_chart.png    # Bar-диаграмма валидные vs невалидные (задача 13)
├── task_09.py         # NumPy-маски: индексы NaN и вне [0,100]
├── task_10.py         # Подсчёт хороших и плохих строк
├── task_11.py         # DataFrame с колонкой ok, первые 10 нарушений
├── task_12.py         # Сохранение marks_clean.csv
├── task_13.py         # Bar-диаграмма → PNG
├── task_14.py         # Flask API: POST CSV → JSON
└── README.md


## Задачи

### Задача 9 — NumPy маски
Загружает `points` в `float`-массив NumPy, строит три маски и возвращает индексы плохих строк.

bash
python task_09.py

NaN-индексы (11): [5, 25, 78, ...]
Вне [0,100] (15): [3, 4, 6, ...]
Все плохие  (26): [3, 4, 5, 6, ...]


### Задача 10 — Подсчёт
На том же массиве считает хорошие и плохие строки.

bash
python task_10.py

Хороших строк : 174
Плохих строк  : 26


### Задача 11 — DataFrame + колонка `ok`
Добавляет булеву колонку `ok` и выводит первые 10 нарушений.

```bash
python task_11.py

    points     ok
3    200.0  False
4    150.0  False
5      NaN  False


### Задача 12 — Сохранение чистого файла
Фильтрует DataFrame, оставляет только валидные строки → `marks_clean.csv`.

bash
python task_12.py


### Задача 13 — Bar-диаграмма

bash
python task_13.py


Сохраняет `marks_chart.png`:

![Bar chart](marks_chart.png)

---

### Задача 14 — Flask API

bash
pip install flask pandas
python task_14.py


**Эндпоинт:** `POST /validate`  
**Тело:** `multipart/form-data`, поле `file` — CSV-файл

bash
curl -X POST http://localhost:5000/validate \
     -F "file=@marks.csv"


**Ответ:**

json
{
  "valid_count": 174,
  "invalid_count": 26,
  "error_indices": [3, 4, 5, 6, 16, 17, 21, 25, 78, 82,
                    96, 113, 120, 135, 140, 141, 142, 144, 146, 147]
}


## Установка зависимостей

bash
pip install numpy pandas matplotlib flask


