import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_data(query):
    # 连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='data_mining', charset='utf8mb4')
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(query)
    # 获取数据
    data = cur.fetchall()
    # 关闭数据库
    cur.close()
    conn.close()
    return data

def get_data_list(query):
    # 连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='data_mining', charset='utf8mb4')
    cur = conn.cursor
