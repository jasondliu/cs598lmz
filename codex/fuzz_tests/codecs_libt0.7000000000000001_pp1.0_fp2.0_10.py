import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 创建数据库连接
conn = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='spider',
    charset='utf8mb4'
)

# 获取游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
result = cursor.execute('select * from test')

# 获取所有结果
print(cursor.fetchall())

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关
