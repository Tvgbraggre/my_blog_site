import dj_database_url

from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.pythonanywhere.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"

db_from_env = dj_database_url.config(
    default='mysql://Tvgbraggre:TTstlyes04#+@Tvgbraggre.mysql.pythonanywhere-services.com/Tvgbraggre$my_blog'
)
DATABASES["default"].update(db_from_env)
