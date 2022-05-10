import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 使用mysql.connector
# 注意把password设为你的root口令:
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test', charset='utf8mb4')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()
# 运
