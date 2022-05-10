import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 执行sql语句
sql = "select * from user"
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()
for row in results:
    print(row)

# 关闭连接
cursor.close()
conn.close()
