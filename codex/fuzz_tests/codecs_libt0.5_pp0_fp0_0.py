import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_connection():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='bilibili',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def get_data(sql):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    finally:
        conn.close()

def insert_data(sql):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

def get_data_from_db(sql):
    conn = get_connection()
    try:
        with conn.cursor() as
