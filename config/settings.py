import os
import environ


# -----------------------------------------------------------------------------
# Basic Config
# -----------------------------------------------------------------------------
env = environ.Env()
root_path = environ.Path(__file__) - 2
env.read_env(env_file=root_path(".env"))
ENV = env("DJ_ENV", default="prod")
assert ENV in ["dev", "test", "prod", "qa"]
DEBUG = env.bool("DJ_DEBUG", default=False)
BASE_DIR = root_path()
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"


# -----------------------------------------------------------------------------
# Security and Users
# -----------------------------------------------------------------------------
SECRET_KEY = env("DJ_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJ_ALLOWED_HOSTS", default=["*"])
CORS_ORIGIN_ALLOW_ALL = True
LOGIN_URL = env("DJ_LOGIN_URL", default="/")
LOGIN_REDIRECT_URL = env("DJ_LOGIN_REDIRECT_URL", default="/")
LOGOUT_URL = env("DJ_LOGOUT_URL", default="/")
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',
]


# -----------------------------------------------------------------------------
# Django Rest Framework
# -----------------------------------------------------------------------------
REST_KNOX = {
    'TOKEN_TTL': None
}
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ]
}


# -----------------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------------
DJANGO_DATABASE_URL = env.db("DJ_DATABASE_URL")
DATABASES = {"default": DJANGO_DATABASE_URL}


# -----------------------------------------------------------------------------
# Static & Media Files
# -----------------------------------------------------------------------------
STATIC_URL = env("DJ_STATIC_URL", default="/static/")
STATIC_ROOT = env("DJ_STATIC_ROOT", default=root_path("static"))
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = env("DJ_MEDIA_URL", default="/media/")
MEDIA_ROOT = env("DJ_MEDIA_ROOT", default=root_path("media"))
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"
ADMIN_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'admin')
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880


# -----------------------------------------------------------------------------
# Application definition
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    # Standard Django libraries
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
    'catalog.apps.CatalogConfig',

    # Libraries
    'knox',
    'rest_framework',

]


# -----------------------------------------------------------------------------
# Time & Language
# -----------------------------------------------------------------------------
LANGUAGE_CODE = env("DJ_LANGUAGE_CODE", default="pt-br")
TIME_ZONE = env("DJ_TIMEZONE", default="America/Recife")
USE_I18N = env("DJ_USE_I18N", default=True)
USE_L10N = env("DJ_USE_L10N", default=True)
USE_TZ = env("DJ_USE_TZ", default=False)


# -----------------------------------------------------------------------------
# Middlewares
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -----------------------------------------------------------------------------
# Templates
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root_path("templates")]
        ,
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
