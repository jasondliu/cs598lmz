import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='spider', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
conn.commit()

# 插入数据
id = '20120001'
user = 'Bob'
age = 20
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    conn.commit()
except Exception as
