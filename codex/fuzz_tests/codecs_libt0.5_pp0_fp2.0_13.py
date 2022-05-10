import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接Mysql数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='test',
    charset='utf8mb4'
)

cursor = conn.cursor()

# sql语句
# sql = 'select * from student'
sql = 'insert into student values(%s,%s,%s)'

# 执行sql语句
cursor.execute(sql, ('1', 'Tom', '1 year 1 class'))

# 提交事务
conn.commit()

# 关闭连接
cursor.close()
conn.close()
