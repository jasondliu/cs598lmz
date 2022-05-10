import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='test', charset='utf8mb4')
cursor = conn.cursor()

# 获取数据库中的所有表名
cursor.execute('show tables')
tables = cursor.fetchall()

# 获取每个表的所有字段
for t in tables:
    cursor.execute('desc %s' % t)
    fields = cursor.fetchall()
    # 获取每个字段的字段名和类型
    for f in fields:
        print(f[0], f[1])

# 关闭数据库连
