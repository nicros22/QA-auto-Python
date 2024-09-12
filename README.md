# Тестовое задание QA

Этот проект содержит 2 папки с разными автоматическими тестами:
1. saucedemo: тесты для сайта [saucedemo.com](https://www.saucedemo.com/).\
    Тесты проверяют функционал авторизации, добавления товаров в корзину и оформления заказа.
2. githubAPI: тест для проверки работы с GitHub API.\
    Тест создает новый репозиторий, проверяет его наличие и затем удаляет его.

## Стек технологий

- Python 3.11
- pytest 8.3.3
- requests 2.32.3
- python-dotenv 1.0.1
- playwright 1.46.0
- pytest-playwright 0.5.2

## Установка

1. Клонируйте репозиторий:
   ```
   git clone git@github.com:nicros22/QA-auto-Python.git
   ```
   
2. Создайте виртуальное окружение и активируйте его:
   ```
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows
   ```
   
3. Перейдите в папку с нужными для вас тестами:
   ```
   cd saucedemo # Для тестов saucedemo
   cd githubAPI # Для теста GitHub API
   ```

4. Дальнейшая инструкция находится в README.md внутри папки с тестами.

## Примечание 
В проекте находятся 2 файла:
- pytest.ini - файл конфигурации pytest, в котором указаны параметры запуска тестов.
- setup.cfg - файл конфигурации flake8, в котором указаны параметры проверки кода.

При установке зависимостей двух проектов, можно запустить оба теста сразу.
Для этого необходимо перейти в корневую папку и выполнить
```
pytest
```
