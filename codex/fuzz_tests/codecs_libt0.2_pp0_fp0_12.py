import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = 'create table if not exists user (id varchar(20) primary key, name varchar(20))'
cursor.execute(sql)

# 插入数据
id = '1'
user = 'Michael'
sql = 'insert into user (id, name) values (%s, %s)'
try:
    cursor.execute(sql, (id, user))
    print('insert success')
    conn.commit()
except:
    print('insert fail')
    conn.rollback()

# 查询数据
sql = 'select * from user where id = %s'
try:
