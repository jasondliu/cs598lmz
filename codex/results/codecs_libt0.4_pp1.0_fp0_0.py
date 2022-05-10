import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_mysql_connection():
    return MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB, charset='utf8mb4')

def get_cursor():
    return get_mysql_connection().cursor()

def execute(query, args):
    cursor = get_cursor()
    cursor.execute(query, args)

def execute_and_fetch_all(query, args):
    cursor = get_cursor()
    cursor.execute(query, args)
    return cursor.fetchall()

def get_id_by_name(name):
    query = "SELECT id FROM users WHERE name = %s"
    result = execute_and_fetch_all(query, (name,))
    if len(result) == 0:
        return None
    else:
        return result[0][0]

def get_name_by_id(user_id):
