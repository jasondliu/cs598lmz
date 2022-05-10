import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 建立数据库连接
conn = pymysql.connect(host='localhost', user='root', password='123456', db='spider', port=3306, charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 创建表
sql = 'create table if not exists t_user (id int primary key auto_increment, name varchar(255), age int, gender varchar(255), address varchar(255))'
cursor.execute(sql)

# 插入数据
sql = "insert into t_user(name, age, gender, address) values(%s, %s, %s, %s)"
cursor.execute(sql, ('张三', 20, '男', '北京'))

# 提交
