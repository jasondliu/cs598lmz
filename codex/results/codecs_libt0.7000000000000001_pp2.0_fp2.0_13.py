import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# config
config = configparser.ConfigParser()
config.read('config.ini')

# mysql conn
mysql_conn = MySQLdb.connect(
    host=config.get('mysql', 'host'),
    port=int(config.get('mysql', 'port')),
    user=config.get('mysql', 'user'),
    passwd=config.get('mysql', 'passwd'),
    db=config.get('mysql', 'db'),
    charset='utf8mb4'
)

# redis conn
redis_conn = redis.Redis(
    host=config.get('redis', 'host'),
    port=int(config.get('redis', 'port')),
    db=int(config.get('redis', 'db')),
    password=config.get('redis', 'passwd')
)

# Create your models here.
class User(models.Model):
    username =
