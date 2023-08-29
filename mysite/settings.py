# import environ
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()



# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY= 'django-insecure-q)2$##7$5s@v+a9=1v$@cxkm8-@wx_#yntjt203@-cn9*etw%j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
# DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'blog',
    'portfolio',

    'crispy_forms',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'sylar_portfolio',
#         'USER': 'sylar',
#         'PASSWORD': 'zT70UNWF6mLckhgAWsXPsVfFw1wpEgus',
#         'HOST': 'ccc.oregon-postgres.render.com',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd9etnvrlqchd65',
#         'USER': 'qnpqpxylvijwpn',
#         'PASSWORD':'d9c56fa93bbc566c4a2adfee33107d666deba76dc287d15c8fb93c62b11cc334',
#         'HOST': 'ec2-34-205-217-14.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bootshop',
#         'USER': 'postgres',
#         'PASSWORD':'12345',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = '587'
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'julius.nartey.71@gmail.com'
EMAIL_HOST_USER = 'sylarnano688@gmail.com'
EMAIL_HOST_PASSWORD = 'ozaxdfucozadbnyu'


# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

AWS_ACCESS_KEY_ID = 'AKIAVR6PCI4EKPRKW4H5'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME ='sylarport'


AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARMETERS = {'CacheControl': 'max-age-86400'}
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = 'portfolio.storage_backends.MediaStorage'

