import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='spider',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
# effect_row = cursor.execute("update hosts set host='1.1.1.2'")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host='1.1.1.3
