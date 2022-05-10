import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 插入数据
def insert_data(data):
    try:
        sql = """INSERT INTO pages (title, content) VALUES (%s, %s)"""
        cur.execute(sql, data)
        conn.commit()
    except pymysql.Error as e:
        print("插入数据失败：" + str(e))

# 查询数据
def select_data():
    try:
        sql = """SELECT * FROM pages"""
        cur.execute(sql)
        print("查
