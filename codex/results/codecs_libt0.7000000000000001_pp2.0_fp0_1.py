import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

# 连接数据库
connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='zhihu',
    charset='utf8mb4'
)

# 获取游标
cursor = connect.cursor()

# 如果表不存在，则创建表
cursor.execute("CREATE TABLE IF NOT EXISTS user_info (id int PRIMARY KEY auto_increment,\
    UserId VARCHAR(20),UserName VARCHAR(20),UserUrlToken VARCHAR(20),UserGender VARCHAR(20),\
    UserLocation VARCHAR(20),UserBusiness VARCHAR(20),UserEmployment VARCHAR(20),\
    UserPosition VARCHAR(20),User
