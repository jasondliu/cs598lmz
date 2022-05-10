import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='scrapy', charset='utf8mb4')
cursor = conn.cursor()

# 创建表
sql = "create table if not exists douban_movie(id int primary key auto_increment, title varchar(255), director varchar(255), " \
      "writer varchar(255), actor varchar(255), type varchar(255), country varchar(255), language varchar(255), " \
      "release_date varchar(255), runtime varchar(255), score varchar(255), votes varchar(255), summary varchar(255))"
cursor.execute(sql)

# 关闭数据库
cursor.close()
