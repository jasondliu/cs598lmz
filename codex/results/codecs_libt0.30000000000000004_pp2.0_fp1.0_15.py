import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql', charset='utf8mb4')
# 创建游标
cur = conn.cursor()
cur.execute("USE scraping")

# 创建数据库
def create_database():
    cur.execute("CREATE DATABASE IF NOT EXISTS scraping")
    cur.execute("USE scraping")
    cur.execute("CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY, title TEXT, content TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS links (fromPageId INTEGER, toPageId INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS websites (id INTEGER PRIMARY KEY,
