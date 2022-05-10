import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mydb', charset='utf8mb4')
cursor = conn.cursor()

# 创建数据库
def createDataBase():
    # 如果数据库不存在则创建
    sql = "create database if not exists mydb"
    cursor.execute(sql)

# 创建表
def createTable():
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()

    # 如果数据表已经存在使用 execute() 方
