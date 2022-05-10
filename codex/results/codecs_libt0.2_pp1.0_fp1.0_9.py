import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = """
create table if not exists user(
    id int primary key auto_increment,
    name varchar(20) not null,
    age int not null,
    gender varchar(10) not null
)
"""
cursor.execute(sql)

# 插入数据
sql = """
insert into user(name, age, gender) values(%s, %s, %s)
"""
cursor.execute(sql, ('张三', 18, '男'))
cursor.execute(sql, ('李四', 19, '女'))
cursor.execute(sql, ('王五
