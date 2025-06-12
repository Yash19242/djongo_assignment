
# Django Internship Assignment Project

This repository is a full-featured backend project developed using **Django**, designed as part of an internship assignment. It demonstrates practical implementation of modern backend concepts such as:

- Django REST Framework (DRF)
- JWT Authentication
- Celery + Redis for background task processing
- Telegram Bot integration
- Secure environment variable management
- Clean and modular project structure

---

## ✅ Features

- **User Authentication** using JWT (Login + Access/Refresh Tokens)
- **Public and Protected API Endpoints**
- **Email Notification** sent via Celery task after user registration
- **Telegram Bot** to collect usernames via `/start` command
- Secure use of `.env` and `python-decouple`
- Structured code for production-readiness
- GitHub version control with clean commit history

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Django 5, Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Task Queue:** Celery with Redis
- **Messaging Bot:** Telegram Bot API
- **Others:** Follows best practices using `.env`, modular structure, Git-based workflow

---

## 📁 Project Structure

```
├── backend/               # Django project settings
├── core/                  # Core app with APIs, models, views, tasks
├── telegram_bot.py        # Telegram bot integration script
├── manage.py
├── .env.example
├── db.sqlite3             # Sample database
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Yash19242/djongo_assignment.git
cd djongo_assignment
```

2. **Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create `.env` file**

Use `.env.example` as a template and add your secrets:

```env
DEBUG=False
SECRET_KEY=your-secret-key
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-app-password
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

5. **Apply migrations & create superuser**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6. **Start Redis (if not already running)**

```bash
redis-server
```

7. **Run Celery in a new terminal**

```bash
celery -A backend worker --loglevel=info
```

8. **Run the development server**

```bash
python manage.py runserver
```

9. **Run the Telegram bot**

```bash
python telegram_bot.py
```

---

## 🔐 API Endpoints

- `GET /api/public/` → Public endpoint
- `GET /api/protected/` → Requires JWT
- `POST /api/login/` → Get JWT token pair

---

## 💬 Telegram Bot

- Bot username: `@SecureRegBot`
- Command: `/start` → Registers Telegram username

---

## 🤝 Contributing

This project is part of a personal learning and evaluation initiative. Contributions are welcome for educational or improvement purposes.

---

## 📄 License

This project is shared for educational purposes and internship evaluation only.
