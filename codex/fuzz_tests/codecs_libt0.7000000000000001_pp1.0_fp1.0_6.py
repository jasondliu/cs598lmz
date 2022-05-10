import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


# 数据库配置
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

# 创建连接
conn = pymysql.connect(**config)

# 创建游标
cursor = conn.cursor()


# 查询一条数据
sql = "SELECT * FROM `user` WHERE `id`=%s"
cursor.execute(sql, (1,))
result = cursor.fetchone()
print(result)

# 查询多条数据
sql
