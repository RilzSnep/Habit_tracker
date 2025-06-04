Habit Tracker
Описание
Приложение для отслеживания привычек с использованием Django, PostgreSQL, Redis, Celery и Nginx.
Локальный запуск

Убедитесь, что установлены Docker и Docker Compose.

Клонируйте репозиторий:
git clone https://github.com/RilzSnep/Habit_tracker
cd Habit_tracker


Создайте файл .env с переменными окружения (см. пример ниже).

Запустите проект:
docker-compose up --build


Приложение будет доступно по адресу http://localhost.


Пример файла .env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=habit_tracker
DB_USER=postgres
DB_PASSWORD=123456
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your-very-secure-secret-key-1234567890
TELEGRAM_BOT_TOKEN=6557371718:AAETC6T-PobT4JXYv0OHM8G40l1BhMp1g

Настройка CI/CD и деплоя
Настройка сервера

Создайте виртуальную машину в Yandex Cloud с Ubuntu 22.04.

Установите Docker и Docker Compose:
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER


Настройте SSH-доступ:

Сгенерируйте SSH-ключ: ssh-keygen -t rsa -b 4096.
Добавьте публичный ключ в ~/.ssh/authorized_keys на сервере.


Клонируйте репозиторий:
git clone https://github.com/RilzSnep/Habit_tracker /home/rilzsnep/habit_tracker



Настройка GitHub Actions

Добавьте секреты в настройки репозитория:
DOCKER_USERNAME и DOCKER_PASSWORD для Docker Hub.
SERVER_HOST, SERVER_USERNAME, SERVER_SSH_KEY для SSH-доступа.


Workflow-файл .github/workflows/ci-cd.yml настроен для:
Линтинга и тестирования.
Сборки и пуша Docker-образов.
Деплоя на сервер.



Адрес сервера

После успешного деплоя приложение доступно по адресу: http://<your-server-ip> (замените на IP сервера).

Minor update
