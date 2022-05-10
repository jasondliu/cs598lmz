import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import pymysql
pymysql.install_as_MySQLdb()

__CONFIG = configparser.ConfigParser()
__SECTION = 'DEFAULT'

try:
	__CONFIG.read(path.join(__FILE__, '..', '..', 'conf', 'config.ini'))
	__BASE_DIR = __CONFIG[__SECTION]['BASE_DIR']
	__DATABASE_HOST = __CONFIG[__SECTION]['DATABASE_HOST']
	__DATABASE_PORT = __CONFIG[__SECTION]['DATABASE_PORT']
	__DATABASE_USERNAME = __CONFIG[__SECTION]['DATABASE_USERNAME']
	__DATABASE_PASSWORD = __CONFIG[__SECTION]['DATABASE_PASSWORD']
	__DATABASE_NAME = __CONFIG[__SECTION][
