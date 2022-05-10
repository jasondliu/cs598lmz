import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='test', charset='utf8mb4')

# 创建游标
cursor = conn.cursor()

# 创建sql语句
sql = "insert into user(name, age) values(%s, %s)"

# 执行sql语句
cursor.execute(sql, ('刘备', 30))

# 提交事务
conn.commit()

# 关闭游标
cursor.close()

# 关闭数据库连接
conn.close()
