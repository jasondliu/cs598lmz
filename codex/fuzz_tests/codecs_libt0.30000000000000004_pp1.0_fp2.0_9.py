import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
def connect_db():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='weibo',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

# 创建数据库
def create_db():
    # 连接数据库
    conn = connect_db()
    # 创建游标
    cursor = conn.cursor()
    # 创建数据库
    cursor.execute('CREATE DATABASE IF NOT EXISTS weibo DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci')
    # 关闭
