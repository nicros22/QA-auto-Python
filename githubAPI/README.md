# GitHub API Tests

## Установка

1. Выполните первые 3 пункта из инструкции в корневой папке проекта.

2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Настройка переменных окружения

1. Создайте файл `.env` в корневой директории проекта.
2. Добавьте следующие строки в файл `.env`, заменив значения на свои (пример - `.env.example`):
   ```
   GITHUB_USERNAME=your_github_username
   GITHUB_TOKEN=your_github_token
   REPO_NAME=test_repo_name
   ```

   Примечание: Для получения персонального токена доступа GitHub, перейдите в Settings -> Developer settings -> Personal access tokens -> Tokens (classic) и создайте новый токен с необходимыми правами (repo).

## Запуск теста

Для запуска теста выполните следующую команду:

```
pytest
```