import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 数据库操作
def save_to_mysql(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

# 关闭数据库连接
cur.close()
conn.close()

# 爬虫设置
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.
