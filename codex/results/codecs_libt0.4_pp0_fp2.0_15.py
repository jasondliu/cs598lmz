import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='stock',
    charset='utf8mb4'
)

# 获取游标
cursor = conn.cursor()

# 查询主题信息
sql_select = "select * from stock_topic"
cursor.execute(sql_select)

# 获取所有记录列表
results = cursor.fetchall()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

# 打印结果
print("topic_id,
