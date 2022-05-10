import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 建立数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("SELECT * FROM students WHERE age >= %s", (21,))

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("UPDATE students SET age = %s WHERE name = %s", (25, 'Bob'))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany("INSERT
