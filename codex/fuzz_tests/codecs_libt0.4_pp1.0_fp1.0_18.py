import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 打开csv文件
csv_file = open('test.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)

# 执行sql语句
sql = "select * from test_table"
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()

# 获取MYSQL里面的数据字段名称
fields = cursor.description

# 写上字段信
