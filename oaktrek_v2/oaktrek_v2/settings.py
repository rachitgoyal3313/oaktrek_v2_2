"""
Django settings for oaktrek_v2 project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%0o=-fj%1o7dl--0(cnl18@%_*a&0okoz+%bjat&=u9wln*q!j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'fontawesomefree',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Store',
    # 'Admin',
    'Profile',
    'Chatbot'
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

ROOT_URLCONF = 'oaktrek_v2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oaktrek_v2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'Profile.User'

LOGIN_URL = 'login'


JAZZMIN_SETTINGS = {
    # Title on the login screen
    "site_title": "OakTrek Admin",
    
    # Title on the brand (top left)
    "site_header": "OakTrek",
    
    # Logo to use for your site
    "site_logo": "assets/logos/patta.png",
    
    # CSS classes for brand element
    "site_brand": "OakTrek",
    
    # Welcome text on the login screen
    "welcome_sign": "Welcome to OaktTrek Admin",
    
    # Copyright on the footer
    "copyright": "OakTrek Ltd",
    
    # The model admin to search from the search bar
    "search_model": ["products.Product", "profile.User"],
    
    # Field name on user model that contains avatar image
    "user_avatar": None,
    
    # Top Menu
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Site", "url": "/", "new_window": True},
    ],
    
    # User Menu
    "usermenu_links": [
        {"name": "Profile", "url": "admin:profile_user_change", "new_window": False},
    ],
    
    # Whether to display the side menu
    "show_sidebar": True,
    
    # Whether to expand the side menu
    "navigation_expanded": False,
    
    # Custom icons for side menu apps/models
    "icons": {
        "products.Product": "fas fa-shopping-bag",
        "products.Review": "fas fa-star",
        "products.Cart": "fas fa-shopping-cart",
        "products.Wishlist": "fas fa-heart",
        "products.Order": "fa-light fa-file-invoice-dollar",
        "profile.User": "fas fa-user",
        "profile.Address": "fas fa-map-marker-alt",
        "auth.Group": "fas fa-users",
    },
    
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",
    
    # Use a custom CSS
    "custom_css": "css/admin.css",
    
    # Custom JS for extra functionality
    "custom_js": "js/admin.js",
    
    # Show UI builder
    "show_ui_builder": True,
    
    # Change form template for specific models
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "products.Product": "collapsible",
        "products.Order": "horizontal_tabs",
    },
    
    # Related modal configuration
    "related_modal_active": True,
}

# UI Tweaks
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

load_dotenv()

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
EMAIL_PORT = 587  # Common port for TLS
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Only one of TLS or SSL should be True
EMAIL_HOST_USER = os.getenv('mail')  # Your email address
EMAIL_HOST_PASSWORD = os.getenv('pass')  # Your email password or app password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
