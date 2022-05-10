import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def build_connection():
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        db="test",
        charset='utf8mb4')
    return con

def insert_data(con, table, item):
    # 得到cursor对象
    cursor = con.cursor()
    # 插入数据
    sql = "INSERT INTO "+table+" (`id`,`title`,`link`,`info`,`content`) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, item)
    # 提交到数据库执行
    con.commit()
    cursor.close()

def select_data(con, table):
    # 得到cursor对象
