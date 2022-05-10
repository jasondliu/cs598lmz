import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 创建表
sql = """create table if not exists students(
        id int(11) primary key auto_increment,
        name varchar(20),
        age int
        )"""
cursor.execute(sql)

# 插入记录
sql = "insert into students(name, age) values(%s, %s)"
cursor.execute(sql, ('张三', 18))
cursor.execute(sql, ('李四', 20))
cursor.execute(sql, ('王五', 22))
# 提交事务
