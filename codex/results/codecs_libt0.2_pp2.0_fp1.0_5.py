import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 执行插入操作
def insert(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.connection.commit()

# 执行查询操作
def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    return [x[0] for x in cur.fetchall()]

#
