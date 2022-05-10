import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import MySQLdb as mdb
import pymysql
import pymysql.cursors

def get_connection():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def get_films_by_actor(actor_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM film_actor WHERE actor_id = %s", (actor_id))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_all_films():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM film")
    rows = cur.f
