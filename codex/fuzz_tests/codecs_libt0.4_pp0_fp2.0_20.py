import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='test',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

def get_connection_with_autocommit():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='test',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    return conn

def execute(query, args={}):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
        conn.commit()
    finally:
        conn.close
