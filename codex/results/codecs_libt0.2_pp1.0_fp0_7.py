import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='root', db='test', charset='utf8mb4')
cur = conn.cursor()

# 读取数据
sql = 'select * from test_table'
cur.execute(sql)
data = cur.fetchall()

# 写入数据
sql = 'insert into test_table values(%s,%s)'
cur.executemany(sql, data)
conn.commit()

# 关闭连接
cur.close()
conn.close()
