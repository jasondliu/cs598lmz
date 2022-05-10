import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='my_db', charset='utf8mb4')
cursor = conn.cursor()

# 执行插入数据
sql = "insert into user(user_id, user_name, user_pwd, user_email) values(%s, %s, %s, %s)"
cursor.execute(sql, ('1', 'tom', '123456', 'tom@qq.com'))
cursor.execute(sql, ('2', 'jerry', '654321', 'jerry@qq.com'))
cursor.execute(sql, ('3', 'kate', '123456', 'kate@qq.com'))
cursor.execute(sql, ('4', 'bob', '654321', 'bob@qq.
