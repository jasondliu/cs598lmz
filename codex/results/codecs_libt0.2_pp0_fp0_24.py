import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='test', port=3306, charset='utf8mb4')
cur = conn.cursor()

# 获取数据
sql = 'select * from test'
cur.execute(sql)
data = cur.fetchall()

# 写入文件
with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name'])
    writer.writerows(data)

# 关闭数据库连接
cur.close()
conn.close()
