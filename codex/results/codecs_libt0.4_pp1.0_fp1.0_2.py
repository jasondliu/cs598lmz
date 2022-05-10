import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 查询记录数
count = cursor.execute('select * from user')
print('total records:', cursor.rowcount)

# 查询一条记录
print('fetch one:', cursor.fetchone())

# 查询多条记录
print('fetch five:', cursor.fetchmany(5))

# 查询所有记录
print('fetch all:', cursor.fetchall())

# 插入一条记录
sql
