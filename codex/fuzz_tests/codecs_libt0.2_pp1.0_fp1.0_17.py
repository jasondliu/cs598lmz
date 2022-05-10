import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='spider', charset='utf8mb4')

# 创建游标
cursor = conn.cursor()

# 创建sql语句
sql = 'insert into students(name, age, score) values(%s, %s, %s)'

# 执行sql语句
cursor.execute(sql, ('Tom', 20, 99))

# 提交事务
conn.commit()

# 关闭游标
cursor.close()

# 关闭数据库连接
conn.close()
