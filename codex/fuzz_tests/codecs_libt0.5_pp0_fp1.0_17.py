import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#
#   Открытие файла настроек
#

with open('settings.json', 'r') as f:
    settings = json.load(f)

#
#   Настройки подключения к MySQL
#

SQL_HOST = settings['mysql']['host']
SQL_PORT = settings['mysql']['port']
SQL_USER = settings['mysql']['user']
SQL_PASS = settings['mysql']['pass']
SQL_DB = settings['mysql']['db']

#
#   Настройки подключения к Redis
#

REDIS_HOST = settings['redis']['host']
REDIS_PORT = settings['red
