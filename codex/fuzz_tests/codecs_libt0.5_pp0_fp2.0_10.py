import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from t_user")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update t_user set nikename=%s where nikename=%s", ('abc', 'abc'))

# 执行SQL，并返回受影响行数,执行多次
# effect
