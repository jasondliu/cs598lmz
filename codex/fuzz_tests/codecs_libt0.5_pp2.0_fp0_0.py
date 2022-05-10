import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY,
            username text NOT NULL,
            password text NOT NULL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
            id integer PRIMARY KEY,
            user_id integer NOT NULL,
            text text NOT NULL,
            created_at text NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )''')

    def add_user(self, username, password):
