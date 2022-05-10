import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset='utf8mb4')
cur = conn.cursor()

# 数据库操作
def insert(sql):
    cur.execute(sql)
    conn.commit()

def select(sql):
    cur.execute(sql)
    return cur.fetchall()

# 数据库操作
def insert_data(sql):
    cur.execute(sql)
    conn.commit()

def select_data(sql):
    cur.execute(sql)
    return cur.fetchall()

# 创建表
def create_table():
    sql = '''
        CREATE TABLE IF NOT EXISTS `test`.
