import threading
threading.stack_size(1024*1024)

def get_connection():
    return sqlite3.connect(DATABASE, check_same_thread=False)

def execute_sql(sql):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except Exception, e:
        print e
        return False
    return True

def query_sql(sql):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
    except Exception, e:
        print e
        return False
    return result

def init_db():
    execute_sql('''
        CREATE TABLE IF NOT EXISTS "user" (
            `uid`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            `username`	TEXT NOT NULL UN
