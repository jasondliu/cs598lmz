import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_connection():
    return MySQLdb.connect(host='localhost', port=3306, user='', passwd='', db='', charset='utf8mb4')

def get_cursor(conn):
    return conn.cursor()

def get_category(conn):
    cur = get_cursor(conn)
    cur.execute("select id, name, sort, parentId from category")
    return cur.fetchall()

def update_category(conn, categoryId, alias):
    cur = get_cursor(conn)
    cur.execute("update category set alias = %s where id = %s", (alias, categoryId))
    conn.commit()

def insert_category(conn, name, sort, parentId, alias):
    cur = get_cursor(conn)
    cur.execute("insert into category (id, name, sort, parentId, alias) values (%s, %s, %s, %s, %s
