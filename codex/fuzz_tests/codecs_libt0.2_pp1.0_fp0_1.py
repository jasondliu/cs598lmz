import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from t_user")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update t_user set name=%s where nid=%s", ("王五", 2))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.execut
