import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 导入 pymysql 库
import pymysql

# 连接数据库, 获取 cursor 对象
def get_cursor():
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'wanglei'
    port = 3306
    db = pymysql.connect(host, user, password, database, port)
    cursor = db.cursor()
    return cursor

# 关闭数据库连接
def close_connect():
    db = pymysql.connect(host, user, password, database, port)
    db.close()


# 获取最新的图片信息
def get_image_info(page):
    cursor = get_cursor()
    sql = 'select *
