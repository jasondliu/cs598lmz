import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
def connect_db():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn

# 插入数据
def insert_db(conn, sql):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

# 查询数据
def select_db(conn, sql):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    except:
        print('Error')

