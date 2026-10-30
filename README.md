# AI Smart Fitness Tracker

A Django-based fitness tracking application with user accounts, fitness dashboard, macro prediction components, workout planning and AI chatbot integration.

## Technology Stack
- Python
- Django
- SQLite
- HTML, CSS and JavaScript

## Setup
1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `.\.venv\Scripts\Activate.ps1`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy configuration: `Copy-Item .env.example .env`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

## Configuration
Configure your Django secret key and required API credentials in .env. Never commit real credentials.

## Important
The current email backend prints messages to the console. External integrations require valid credentials. Production deployment requires additional security configuration.
