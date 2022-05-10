import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 执行SQL查询
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
