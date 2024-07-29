# reloqcypr

###
- Python 3.10

### Steps

1. Создаем и активируем виртуальное окружение:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```
3. Устанавливаем либы:
    ```sh
    pip install -r requirements.txt
    ```
4. Инициализируем RASA
    ```sh
    rasa init

    enter
    y
    n
    ```
5. Копируем в Data nlu.yml,  rules.yml, stories.yml, cyprus-bot-data.json

6. Копируем в главную директорию domain.yml, config.yml

7. Указать свои данные для credentails.yml(закину в личку), снимаем кодировку в endpoints

8. Копируем в директорию actions actions.py, llmbot.py load.py, query_llm.py ОБЯЗАТЕЛЬНО УКАЗАТЬ СВОИ ПУТИ ВНУТРИ ФАЙЛОВ!

9. Загружаем модель
     ```sh
    python load.py
    ```
10. Тренеруем и запускаем RASA rasa run action и rasa run в отдельных командных строках
    ```sh
    rasa train
    rasa run action
    rasa run
    ```
