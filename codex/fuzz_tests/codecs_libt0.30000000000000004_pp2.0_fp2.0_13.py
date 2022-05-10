import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("update user set name='%s' where id = %s" % ('李四', 1))

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update user set name=%s where id = %s", ('李四', 1))

# 执行SQL，并返回受影
