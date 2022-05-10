import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

#设置相关参数
host = "localhost"
port = 3306
user = "root"
password = "root"
db = "db_phonedata"
charset = "utf8mb4"

#数据库连接
conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)

def insert_data(sql, values):
    try:
        with conn.cursor() as cursors:
            cursors.execute(sql, values)
        conn.commit()
    except Exception as e:
        print(e)

def select_data(sql):
    try:
        with conn.cursor() as cursors:
            cursors.execute(sql)
        rows = cursors.fetchall()
        # print(rows)
        return rows

