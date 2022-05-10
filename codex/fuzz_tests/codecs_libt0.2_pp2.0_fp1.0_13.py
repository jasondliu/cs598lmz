import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='test', charset='utf8mb4')
cur = conn.cursor()

# 创建表
cur.execute("create table if not exists student(id int primary key auto_increment, name varchar(255), age int)")

# 插入数据
cur.execute("insert into student(name, age) values(%s, %s)", ('张三', 20))
cur.execute("insert into student(name, age) values(%s, %s)", ('李四', 21))
cur.execute("insert into student(name, age) values(%s, %s)", ('王五', 22))
cur.execute("insert into student(name, age) values(%s, %s)", ('
