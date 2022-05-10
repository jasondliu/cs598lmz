import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydb', port=3306, charset='utf8mb4')
cursor = db.cursor()

sql = "SELECT * FROM users"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        email = row[2]
        password = row[3]
        mobile = row[4]
        # 打印结果
        print "id=%s,name=%s,email=%s,password=%s,mobile=%s" % \
              (id, name, email, password, mobile)
except:
    print "Error: unable to fecth data"

# 关闭数据库连接
db.close()
