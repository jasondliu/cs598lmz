import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 查询数据
sql = "select * from test"
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()
for row in results:
    id = row[0]
    name = row[1]
    print("id=%s,name=%s" % \
          (id, name))

# 关闭连接
cursor.close()
conn.close()
