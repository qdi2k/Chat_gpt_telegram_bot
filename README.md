# Chat GPT Telegram_bot

Телеграм бот для общение с ChatGPT. Бот реализован на библиотеке Aiogram3,
с использованием токена Llama для генерации текста и ответов OpenAI.
Для отслеживания работы бота все события и действия записываются в файл.

---

### Быстрый старт

1. Склонируйте проект на свой компьютер
2. Сгенерируйте Llama токен по официальному [руководству](https://docs.llama-api.com/api-token) 
3. Создайте файл `.env` и наполните его в предложенном формате
```
TG_TOKEN=123456789 # Токен вашего telegram бота 
LLAMA_TOKEN=123456789 # Ваш токен Llama 
```
4. Если у вас нет виртуального окружения, то создайте и  активируйте его
```shell
python -m venv venv
```
```shell
venv\Scripts\activate.bat
```
5. Обновите pip и установите необходимые зависимости
```shell
pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```
6. Запустите run.py
```shell
python run.py
```

---

