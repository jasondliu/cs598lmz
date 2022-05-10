import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_connection():
    return MySQLdb.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        db = 'test',
        charset = 'utf8mb4',
        use_unicode = True
    )

def get_cursor(connection):
    return connection.cursor()

def execute_query(query):
    connection = get_connection()
    cursor = get_cursor(connection)
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

def execute_query_fetch_one(query):
    connection = get_connection()
    cursor = get_cursor(connection)
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

def execute_query_fetch_all(query):
    connection = get_connection()

