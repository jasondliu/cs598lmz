import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 配置数据库连接
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flask_demo'
# 配置数据库连接池
SQLALCHEMY_POOL_SIZE = 100
# 配置数据库自动提交
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
# 配置数据库追踪修改
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 配置redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD =
