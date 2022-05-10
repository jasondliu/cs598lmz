import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 定义数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', db='spider', port=3306, charset='utf8mb4')
# 创建游标
cursor = db.cursor()

# 定义爬虫类
class Spider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        self.proxies = {
            'http': 'http://61.135.217.7
