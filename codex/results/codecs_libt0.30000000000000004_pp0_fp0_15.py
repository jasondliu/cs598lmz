import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='test', charset='utf8mb4')
cur = conn.cursor()

# 读取数据
sql = 'select * from test.test_table'
cur.execute(sql)

# 获取数据
rows = cur.fetchall()

# 写入数据
with open('data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# 关闭数据库
cur.close()
conn.close()
