import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 加载配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# 连接数据库
db = pymysql.connect(host=config['mysql']['host'],
                     port=int(config['mysql']['port']),
                     user=config['mysql']['user'],
                     passwd=config['mysql']['passwd'],
                     db=config['mysql']['db'],
                     charset=config['mysql']['charset'])
cursor = db.cursor()

# 连接redis
redis_pool = redis.ConnectionPool(host=config['redis']['host'],
                                  port=int(config['redis']['port']),
                                  db=int(config['redis']['db
