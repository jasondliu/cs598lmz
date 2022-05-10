import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='spider', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = 'create table if not exists t_spider (id int primary key auto_increment, title varchar(200), link varchar(200), content text)'
cursor.execute(sql)

# 插入数据
sql = 'insert into t_spider (title, link, content) values (%s, %s, %s)'
cursor.execute(sql, ('标题', 'http://www.baidu.com', '内容'))

# 提交事务
conn.commit()

# 关闭连
