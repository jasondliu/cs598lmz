import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql', charset='utf8mb4')
# 创建游标
cur = conn.cursor()

# 执行SQL，并返回收影响行数
# effect_row = cur.execute("select * from user")
# effect_row = cur.execute("update user set password='123' where id=1")
# effect_row = cur.execute("delete from user where id=1")
# effect_row = cur.execute("insert into user(id, username, password) values(1, 'tom', '123')")

# 执行SQL，并返回受影响行数

