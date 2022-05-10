import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', password='123456', database='test', charset='utf8mb4')

# 创建游标
cursor = conn.cursor()

# 执行查询
cursor.execute('select * from user')

# 获取结果集
result_set = cursor.fetchall()

# 打印结果集
for row in result_set:
    print('id:', row[0], 'name:', row[1])

# 关闭游标
cursor.close()

# 关闭数据库连接
conn.close()
