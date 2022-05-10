import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_connection():
    return MySQLdb.connect(host='localhost', user='root', passwd='', db='crawler', charset='utf8mb4')

def get_cursor():
    con = get_connection()
    return con.cursor()

def get_cursor_dict():
    con = get_connection()
    return con.cursor(MySQLdb.cursors.DictCursor)

def get_cursor_dict_utf8():
    con = get_connection()
    return con.cursor(MySQLdb.cursors.DictCursor)

def execute_query(query):
    cursor = get_cursor()
    cursor.execute(query)
    return cursor.fetchall()

def execute_query_dict(query):
    cursor = get_cursor_dict()
    cursor.execute(query)
    return cursor.fetchall()

def execute_query_dict_
