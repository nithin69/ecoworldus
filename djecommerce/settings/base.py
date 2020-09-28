import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    # 'material.admin',
    # 'material.admin.default',
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'pagedown.apps.PagedownConfig',
    'markdownify',
    'markdown_deux',
    'mathfilters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'djecommerce.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MARKDOWNIFY_STRIP = False
MARKDOWNIFY_WHITELIST_TAGS = {'*'}

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

EMAIL_HOST = 'smtp-mail.outlook.com' # double check the settings in your outlook mailbox to make sure the host name is correct

EMAIL_PORT = 587  # double check the settings in your outlook mailbox and make sure the port number is correct

EMAIL_HOST_USER = 'info@ecoworldus.com'  # don't include the @blah.com part! I have made this stupid mistakes before

EMAIL_HOST_PASSWORD = 'Manoj@967'

EMAIL_USE_TLS = True

EMAIL_USE_SSL = False


##EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp-mail.outlook.com' # double check the settings in your outlook mailbox to make sure the host name is correct

# EMAIL_PORT = 587  # double check the settings in your outlook mailbox and make sure the port number is correct

# EMAIL_HOST_USER = 'info@ecoworldus.com'  # don't include the @blah.com part! I have made this stupid mistakes before

# EMAIL_HOST_PASSWORD = 'Manoj@967'

# EMAIL_USE_TLS = True

# EMAIL_USE_SSL = False