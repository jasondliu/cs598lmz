import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 建立数据库连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test', charset='utf8mb4')
# 创建游标
cursor = conn.cursor()

# 创建数据表
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# cursor.execute(sql)

# 插入数据
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE
