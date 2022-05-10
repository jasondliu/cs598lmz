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
sql = "INSERT INTO user (id, name) VALUES (6, 'name6')"
cursor.execute(sql)
connect.commit()
print(cursor.rowcount)

# 更新数据
sql = "UPDATE user SET name = 'name7' WHERE id = 6"
cursor.execute(sql)
connect.commit()
print(cursor.rowcount)

# 删除数据
sql = "DELETE FROM user WHERE
