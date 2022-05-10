import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('db.db')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL)''')

    def insert_user(self, username, password, role = 'user'):
        self.cursor.execute('''INSERT INTO users(username, password, role)
            VALUES(?, ?, ?)''', (username, password, role))

    def get_user(self, username):
        self.cursor.execute('''SELECT * FROM users WHERE username = ?''
