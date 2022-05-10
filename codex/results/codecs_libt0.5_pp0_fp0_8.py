import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

import sys
sys.path.append('../..')
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB, MYSQL_CHARSET

def get_mysql_conn():
    conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DB, charset=MYSQL_CHARSET)
    cursor = conn.cursor()
    return conn, cursor

def close_mysql_conn(conn, cursor):
    cursor.close()
    conn.close()

def get_all_tag_id():
    conn, cursor = get_mysql_conn()
    select_sql = "select id from tag"
    cursor.execute(select_sql)
    res = cursor.fetch
