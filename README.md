Habit Tracker
Обзор
Habit Tracker — это веб-приложение на базе Django, предназначенное для отслеживания ежедневных привычек пользователей. Оно включает функции аутентификации пользователей, создания привычек и напоминаний через Telegram-бота. Проект использует Docker для деплоя и Celery для обработки фоновых задач.
Возможности

Регистрация и аутентификация пользователей (через Django REST Framework и JWT).
Создание, обновление и удаление привычек.
Отслеживание выполнения привычек через простой интерфейс.
Получение напоминаний через Telegram-бота.
Документация API с использованием drf-yasg (Swagger).
Автоматизированный CI/CD пайплайн с GitHub Actions.

Технологический стек

Бэкенд: Django, Django REST Framework
База данных: PostgreSQL
Очередь задач: Celery, Redis
Фронтенд: Базовые шаблоны (можно расширить с помощью фреймворка фронтенда)
Деплой: Docker, Docker Compose, Nginx
CI/CD: GitHub Actions
Дополнительные инструменты: drf-yasg (документация API), pytest (тестирование), flake8 (линтинг)

Требования

Python 3.12
Docker и Docker Compose
Git
Токен Telegram-бота (для напоминаний)
Доступ к серверу для деплоя (например, VM)

Установка
1. Клонирование репозитория
git clone https://github.com/RilzSnep/Habit_tracker.git
cd Habit_tracker

2. Настройка переменных окружения
Создайте файл .env в корневой директории проекта и добавьте следующее:
SECRET_KEY=ваш-секретный-ключ
TELEGRAM_BOT_TOKEN=ваш-токен-telegram-бота
DB_ENGINE=django.db.backends.postgresql
DB_NAME=habit_tracker
DB_USER=ваш-пользователь-базы
DB_PASSWORD=ваш-пароль-базы
DB_HOST=db
DB_PORT=5432

3. Сборка и запуск с Docker
docker-compose up --build -d

4. Применение миграций
docker-compose exec web python manage.py migrate

5. Доступ к приложению

Веб-приложение: http://localhost:8000
Документация API (Swagger): http://localhost:8000/swagger/

Запуск тестов
docker-compose exec web python manage.py test habits.tests
docker-compose exec web python manage.py test users.tests

Линтинг
docker-compose exec web flake8 . --max-line-length=200 --exclude=venv,.git,__pycache__

Деплой
Проект использует GitHub Actions для CI/CD. Для деплоя на сервер:

Настройте следующие секреты в вашем репозитории GitHub:
DOCKER_USERNAME и DOCKER_PASSWORD (для логина в Docker Hub)
SERVER_HOST, SERVER_USERNAME, SERVER_SSH_KEY (для SSH-доступа к серверу)


Отправьте изменения в ветку master или feature/homework-ci-cd, чтобы запустить пайплайн.


