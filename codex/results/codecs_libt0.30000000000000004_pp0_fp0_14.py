import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 执行sql语句
sql = 'select * from users'
cursor.execute(sql)

# 获取查询结果
result = cursor.fetchall()
print(result)

# 关闭游标
cursor.close()

# 关闭连接
conn.close()
