import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 创建数据库连接
db = pymysql.connect(host='localhost', user='root', password='root', db='crawler', charset='utf8mb4')
cursor = db.cursor()

# 创建redis连接
redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb
