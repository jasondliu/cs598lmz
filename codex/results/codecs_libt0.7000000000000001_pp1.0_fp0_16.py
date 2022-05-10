import codecs
codecs.register(
    lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
def connect_to_database():
    return pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='root',
                           db='laotu',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

def query(sql):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()

def execute(sql):
    conn = connect_to_database()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            print('insert data success')
            conn.commit()
    finally:
        conn.close()

def dictfetchall(cursor):
    "Return all
