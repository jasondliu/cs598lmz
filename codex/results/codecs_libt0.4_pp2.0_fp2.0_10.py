import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
MYSQL_DB = 'weibo'

# MongoDB
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'weibo'
MONGO_COLLECTION = 'weibo'

# Redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DB = 0

# Proxy
PROXY_POOL_URL = 'http://127.0.0.1:5555/random'

# KeyWord
KEYWORD = '风景'

# Time
START_TIME = '2017-01-01'
END_TIME = '2017
