import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cur = con.cursor()

sql = 'select * from test_data where id = %s'

cur.execute(sql, (1,))
print(cur.fetchone())

cur.close()
con.close()

# 注意：如果执行了select语句，返回的是元组列表，如果执行了insert、update、delete，返回的是int型的受影响的行数
# 注意：如果是高并发的环境下
