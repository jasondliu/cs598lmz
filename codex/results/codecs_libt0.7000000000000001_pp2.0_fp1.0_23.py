import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


def get_cursor(dbname):
    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            db=dbname,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(e)
    return conn


def get_data(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data


def insert_data(conn, sql, data):
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def create_table(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


if __
