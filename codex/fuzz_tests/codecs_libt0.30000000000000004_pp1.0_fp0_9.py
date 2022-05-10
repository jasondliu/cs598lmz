import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql', charset='utf8mb4')
# 创建游标
cur = conn.cursor()
cur.execute("USE scraping")

# 创建数据库
# cur.execute("CREATE DATABASE scraping")
# cur.execute("USE scraping")

# 创建表
# cur.execute("CREATE TABLE pages (id INTEGER PRIMARY KEY, title VARCHAR(255), content TEXT)")

# 插入数据
# cur.execute("INSERT INTO pages (title, content) VALUES ('Test title', 'Test content')")
# cur.execute("INSERT INTO pages (title, content) VALUES ('
