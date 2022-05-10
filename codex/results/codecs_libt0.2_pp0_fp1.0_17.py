import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='test',
    charset='utf8mb4'
)

# 获取游标
cursor = connect.cursor()

# 插入数据
sql = "INSERT INTO user (id, name) VALUES (1, 'Tom')"
cursor.execute(sql)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')

# 修改数据
sql = "UPDATE user SET name = 'Jack' WHERE id = %s"
cursor.execute(sql, (1,))
connect.commit()
print('成功修
