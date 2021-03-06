import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 打开数据库连接
db = pymysql.connect("localhost","root","123456","test",charset='utf8mb4')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚

