import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mysql', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE scraping")

# 执行sql语句
def insert_data(data):
    try:
        sql = """INSERT INTO pages (title, content) VALUES (%s, %s)"""
        cur.execute(sql, data)
        conn.commit()
    except pymysql.Error as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

# 关闭数据库
def close_db():
    cur.close()
    conn.close()

# 创建表
def create_
