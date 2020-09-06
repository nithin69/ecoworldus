from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = 'pk_live_51HIgs4EC9akyPN5UX4q3kcwbaFUfUw608tpLKRKHkmxphSSI34J0tyFfBBsfT0JMdQ5bPu2UXfZKxniX6eMo8tue001MQ4a4zt'
STRIPE_SECRET_KEY = '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'