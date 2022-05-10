import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute('USE wikipedia')

# 定义一个函数，用来获取URL并抓取数据
def getLinks(fromPageId):
    cur.execute('SELECT toPageId FROM links WHERE fromPageId = %s', (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

# 定义一个函数，用来获取指定ID的URL
def getUrl(pageId):
