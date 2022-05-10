import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL configurations
# mysql的配置信息

# mysql的配置信息

MYSQL_HOSTname = '127.0.0.1'
MYSQL_USERNAME = 'root'
MYSQL_PORT='3306'
MYSQL_PASSWORD = '199733'
MYSQL_DATABASE = 'test'

# MYSQL_HOSTname = '127.0.0.1'
# MYSQL_USERNAME = 'root'
# MYSQL_PASSWORD = 'root'
# MYSQL_DATABASE = 'mydatabase'
# MYSQL_PORT = 3306
# MYSQL_CHARSET = 'utf8mb4'



#服务端的url
SERVER_URL = 'http://127.0.0.1:5000/'

# 当前
