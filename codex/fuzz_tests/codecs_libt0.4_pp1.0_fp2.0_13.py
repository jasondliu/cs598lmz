import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 以下是配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'news'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PORT = 3306

# 指定抓取时间跨度
TIME_SPAN = 1

# 指定抓取的起止时间
BEGIN_DATE = '2016-01-01'
END_DATE = '2016-08-01'

# 指定抓取的新闻类别
CATEGORIES = {u'科技': 'tech',
              u'教育': 'edu',
              u'军事': 'mil',
             
