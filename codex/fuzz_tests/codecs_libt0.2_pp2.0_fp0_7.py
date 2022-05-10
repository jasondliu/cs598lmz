import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test', port=3306, charset='utf8mb4')
cur = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cur.execute("select * from user")

# 执行SQL，并返回受影响行数
# effect_row = cur.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cur.executemany("insert into
