import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 数据库配置
DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'test',
    'charset': 'utf8mb4'
}

# 创建连接
conn = pymysql.connect(**DB_CONFIG)

# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from tb1")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update tb1
