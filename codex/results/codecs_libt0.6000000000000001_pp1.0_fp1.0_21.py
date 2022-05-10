import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回受影响行数
# 删除表
effect_row = cursor.execute("drop table if exists student")
print(effect_row)

# 创建表
effect_row = cursor.execute("create table student(id int unsigned auto_increment primary key,name varchar(20),class varchar(30),age tinyint unsigned)")

# 插入一条数据
effect_row = cursor.execute("insert into student(name,
