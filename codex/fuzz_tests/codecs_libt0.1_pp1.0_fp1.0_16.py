import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test', charset='utf8mb4')
cursor = conn.cursor()

# 查询数据
sql = "select * from user"
cursor.execute(sql)

# 获取所有记录列表
results = cursor.fetchall()
for row in results:
    fname = row[0]
    lname = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    # 打印结果
    print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
          (fname, l
