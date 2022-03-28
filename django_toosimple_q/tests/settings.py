"""Settings for running tests"""

"""Settings overrides for testing concurrent workers"""

import os

DEBUG = True
USE_TZ = True
TIME_ZONE = "UTC"
SECRET_KEY = "secret_key"


if os.getenv("TOOSIMPLEQ_TEST_DB", "sqlite") == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": "127.0.0.1",
            "PORT": "5432",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "TEST": {
                "NAME": "test_postgres",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "db.sqlite3",
            "OPTIONS": {"timeout": 50},
            "TEST": {
                "NAME": "db-test.sqlite3",
            },
        }
    }

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django_toosimple_q",
    "django_toosimple_q.tests.concurrency",
]

ROOT_URLCONF = "django_toosimple_q.tests.urls"

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ]
        },
    }
]

STATIC_URL = "/static/"
