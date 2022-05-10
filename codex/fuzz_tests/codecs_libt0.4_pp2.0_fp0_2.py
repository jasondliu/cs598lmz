import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 数据库操作
def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

# 测试数据库操作
# store("测试标题", "测试内容")
# cur.execute("SELECT * FROM pages")
# print(cur.fetchone())

# 关闭连接
cur.close()
conn.close()
