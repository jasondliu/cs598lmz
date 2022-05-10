import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='DOUBAN', port=3306, charset='utf8mb4')
cur = conn.cursor()

# 创建数据表
# cur.execute('create table Books(id int primary key auto_increment, name varchar(128), author varchar(128), press varchar(128), year varchar(128), price varchar(128), rating decimal(3,1), rating_people int, comments int, ISBN varchar(128))')

# 查询操作
# cur.execute('select * from Books')
# data = cur.fetchall()
# for d in data:
#     print(d)
# cur.close()
# conn.close()

#
