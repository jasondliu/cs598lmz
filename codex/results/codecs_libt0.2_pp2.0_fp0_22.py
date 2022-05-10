import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 创建数据库
def create_database():
    cur.execute("CREATE DATABASE IF NOT EXISTS scraping")
    cur.execute("USE scraping")
    cur.execute("CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY, title TEXT, content TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS links (from_page INTEGER, to_page INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS websites (url TEXT, title TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS backlinks (
