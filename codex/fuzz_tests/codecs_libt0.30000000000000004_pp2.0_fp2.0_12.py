import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='spider', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from douban_movie")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update douban_movie set name = '%s' where id = %s" % ('疯狂的石头', 1))

# 执行SQL，并返回受影响行
