import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = "create table if not exists user (id int primary key auto_increment, name varchar(255) not null, age int not null)"
cursor.execute(sql)

# 插入数据
sql = "insert into user(name, age) values(%s, %s)"
cursor.execute(sql, ('张三', 20))
cursor.execute(sql, ('李四', 25))
cursor.execute(sql, ('王五', 30))

# 提交事务
conn.commit()

# 查
