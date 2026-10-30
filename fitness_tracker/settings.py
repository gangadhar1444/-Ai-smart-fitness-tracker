import os
from pathlib import Path
from decouple import config
from dotenv import load_dotenv
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file at the project root
load_dotenv(os.path.join(BASE_DIR, '.env'))

# ------------------ SECURITY ------------------
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed hosts for your Django application. '*' means all hosts (USE WITH CAUTION IN PRODUCTION!)
# In production, change this to your actual domain names (e.g., ['yourdomain.com', 'www.yourdomain.com'])
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# ------------------ APPLICATIONS ------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'corsheaders',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Essential for serving static files
    'core',                       # Your core application
    'django.contrib.humanize',    # Useful for human-readable numbers/dates
]

# ------------------ MIDDLEWARE ------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Add this after SecurityMiddleware
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'fitness_tracker.urls' # Your project's main URL configuration

# ------------------ TEMPLATES ------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS specifies a list of directories where Django should look for template files
        # It's good practice to have a project-level 'templates' folder.
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # APP_DIRS tells Django to look for a 'templates' folder inside each installed app.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fitness_tracker.wsgi.application'

# ------------------ DATABASE ------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# ------------------ AUTHENTICATION ------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_URL = 'login' # URL for the login page
LOGOUT_REDIRECT_URL = 'login' # Where to redirect after logout

# ------------------ INTERNATIONALIZATION ------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata' # Set this to your local timezone (e.g., 'America/New_York', 'Europe/London')
USE_I18N = True # Enable Django's internationalization system
USE_TZ = True # Enable timezone support

# ------------------ STATIC FILES (CSS, JS, Images like workout GIFs, default profile pic) ------------------
# STATIC_URL is the URL prefix for static files.
# When you use {% static 'path/to/file' %}, it resolves to /static/path/to/file
STATIC_URL = '/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # Your project-level static directory
    # --- ADD THIS LINE FOR DIAGNOSIS ---
    os.path.join(BASE_DIR, 'core', 'static'), # Explicitly tell Django to look in core/static/
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS is a list of directories where Django will search for static files
# that are *not* tied to a specific app (e.g., project-wide CSS, JS, or images).
# This should point to your project's 'static' directory if you have one outside of apps.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# STATIC_ROOT is the absolute path to the directory where 'python manage.py collectstatic'
# will gather all static files for deployment (e.g., all app static files + STATICFILES_DIRS).
# This directory should ideally be empty before running collectstatic.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# ------------------ MEDIA FILES (User Uploaded Content like profile images) ------------------
# MEDIA_URL is the URL prefix for media files.
# When a user uploads a file, it will be accessible via /media/path/to/file
MEDIA_URL = '/media/'

# MEDIA_ROOT is the absolute path to the directory where user-uploaded files will be stored.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ------------------ DEFAULT PRIMARY KEY FIELD TYPE ------------------
# Default primary key field type for models added in Django 3.2+
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------ TWILIO (if used) ------------------
TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default='')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default='')
TWILIO_PHONE_NUMBER = config('TWILIO_PHONE_NUMBER', default='')

# ------------------ EMAIL (if used) ------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

FAST2SMS_API_KEY = os.environ.get("FAST2SMS_API_KEY", "")
GEMINI_MODEL_ID = "gemini-2.5-flash"
GEMINI_MODEL_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@example.com'
