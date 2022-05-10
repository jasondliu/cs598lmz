import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用pymysql模块
import pymysql
pymysql.install_as_MySQLdb()

# 使用django-crontab
from django_crontab.crontab import Crontab
Crontab().install()

# 使用django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True

# 使用django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)

# 使用django-extensions
INSTALLED_APPS += ('django_extensions',)

# 使用django-redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
       
