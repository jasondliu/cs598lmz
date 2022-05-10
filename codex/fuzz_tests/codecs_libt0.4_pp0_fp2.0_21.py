import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     db='spider',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

# 创建爬虫类
class Spider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        self.i = 0

    # 发送请
