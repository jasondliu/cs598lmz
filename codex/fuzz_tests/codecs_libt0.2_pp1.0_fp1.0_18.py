import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 插入数据
sql = "insert into user(id, name) values(%s, %s)"
cursor.execute(sql, ('1', 'Michael'))
print(cursor.rowcount)

# 提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute("select * from user where id = %s", ('1',))
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection
cursor.close()

