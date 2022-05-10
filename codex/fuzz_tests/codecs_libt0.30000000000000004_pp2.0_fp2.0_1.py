import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_connection():
    return sqlite3.connect('db.sqlite3')

def get_cursor():
    return get_connection().cursor()

def create_table():
    cursor = get_cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, created_at TEXT)')

def insert_post(title, content):
    cursor = get_cursor()
    cursor.execute('INSERT INTO posts(title, content, created_at) VALUES(?, ?, DATETIME("now", "localtime"))', (title, content))
    get_connection().commit()

def get_posts():
    cursor = get_cursor()
    cursor.execute('SELECT * FROM posts')
    return cursor.fetchall()

def get_post(id):
    cursor = get_cursor()
    cursor.execute('
