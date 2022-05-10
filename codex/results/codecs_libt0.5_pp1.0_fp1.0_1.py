import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库配置
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'spider',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

# 创建连接
connection = pymysql.connect(**config)

try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 创建sql语句
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # 执行sql语句
        cursor.execute(sql, ('webmaster
