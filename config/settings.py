"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from config import my_settings

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = my_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
     # cors
    'corsheaders',
    'common.apps.CommonConfig',  # 로그인 기능을 위함
    'django.contrib.sites',  # 웹 앱(kodeal)과 django-allauth를 연결
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # provider - google
    'allauth.socialaccount.providers.google',

    # blog
    'blog.apps.BlogConfig',
    'rest_framework',

    ## ssl
    'sslserver',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',    # cors 설정
    'django.middleware.common.CommonMiddleware',    # cors 설정
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',    # csrf를 이용하여 로그인 진행을 위해 주석 처리
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = my_settings.DATABASES

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 로그인이 성공한 뒤 이동 URL
LOGIN_REDIRECT_URL = '/'
# 로그아웃이 성공한 뒤 이동 URL
LOGOUT_REDIRECT_URL = '/'

# Custom User Model 로그인 및 회원가입 시 필요
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin(allauth)
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods(ex: email, ...)
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
AUTH_USER_MODEL = 'common.User'

# 이메일 발송 코드 리팩토링
EMAIL_BACKEND = my_settings.EMAIL['EMAIL_BACKEND']
EMAIL_USE_TLS = my_settings.EMAIL['EMAIL_USE_TLS']
EMAIL_PORT = my_settings.EMAIL['EMAIL_PORT']
EMAIL_HOST = my_settings.EMAIL['EMAIL_HOST']
EMAIL_HOST_USER = my_settings.EMAIL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = my_settings.EMAIL['EMAIL_HOST_PASSWORD']
SERVER_EMAIL = my_settings.EMAIL['SERVER_EMAIL']
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 응답 메일 관련 설정

# CSRF 토큰 설정(ajax 통신 시)
CORS_ORIGIN_ALLOW_ALL = True    # 모든 호스트에 대해 cross-site 요청 허용(cors 및 csrf 설정)
CORS_ALLOW_CREDENTIALS = True   # 쿠키가 cross-site HTTP 요청에 포함될 수 있음

CSRF_TRUSTED_ORIGINS = (
    'localhost:8000',
    '127.0.0.1:8000',
    'https://main.d1nielb0ge84b3.amplifyapp.com/',
)
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:8000',
                         'http://localhost:8000',
                         'https://main.d1nielb0ge84b3.amplifyapp.com/',]

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'access-control-allow-credentials',
    'access-control-allow-origin',
    'access-control-request-method',
    'access-control-request-headers',
    'accept',
    'accept-encoding',
    'accept-language',
    'authorization',
    'connection',
    'content-type',
    'dnt',
    'credentials',
    'host',
    'origin',
    'user-agent',
    'X-CSRFToken',
    'csrftoken',
    'x-requested-with',
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cookie 만료 시점 설정
MINUTE = 60
SESSION_COOKIE_AGE = MINUTE * 60		# 쿠키의 유효 기간 설정 (default: 2주)
# SESSION_SAVE_EVERY_REQUEST = True   # 서버에게 Request를 보내면 시간 초기화
