import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


def get_key():
    with open('key.txt', 'r') as f:
        key = f.read()
    return key


def get_token():
    with open('token.txt', 'r') as f:
        token = f.read()
    return token


def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='postgres',
        port=5432
    )


def get_cursor():
    return get_connection().cursor()


def get_last_update_id(cursor):
    cursor.execute('SELECT id FROM updates ORDER BY id DESC LIMIT 1')
    return cursor.fetchone()[0]


def insert_update(cursor, update_id, message):
    cursor.execute(
        'INSERT INTO updates (id, message) VALUES (%s, %s)',
