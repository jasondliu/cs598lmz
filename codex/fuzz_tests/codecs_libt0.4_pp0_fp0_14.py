import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
def connectdb():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
    return db

# 关闭数据库
def closedb(db):
    db.close()

# 插入数据
def insertdb(db,data):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    sql = "INSERT INTO weibo(id,name,time,content,repost_num,comment_num,like_num) VALUES ('%s', '%s', '%s', '%s', '%s', '%
