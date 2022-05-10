import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test', port=3306, charset='utf8mb4')
cur = conn.cursor()

# 创建表
sql = 'create table if not exists test(id int primary key auto_increment, name varchar(20))'
cur.execute(sql)

# 插入数据
sql = 'insert into test(name) values(%s)'
cur.execute(sql, ('测试'))

# 提交事务
conn.commit()

# 关闭连接
cur.close()
conn.close()
