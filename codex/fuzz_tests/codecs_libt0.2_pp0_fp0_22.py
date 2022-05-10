import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 创建表
cur.execute("CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY, title TEXT, content TEXT)")

# 插入数据
cur.execute("INSERT INTO pages (title, content) VALUES ('Test title', 'Test content')")
cur.connection.commit()

# 查询数据
cur.execute("SELECT * FROM pages WHERE title LIKE '%test%'")
print(cur.fetchone())
cur.close()
conn.close()
