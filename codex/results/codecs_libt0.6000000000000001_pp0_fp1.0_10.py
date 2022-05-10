import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test', port=3306, charset='utf8')
cur = conn.cursor()

# 创建表
sql = 'create table if not exists user (id varchar(20) primary key, name varchar(20))'
# 执行SQL语句
cur.execute(sql)
# 提交到数据库执行
conn.commit()

# 关闭数据库连接
conn.close()
