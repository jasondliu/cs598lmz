import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

    def create_table(self, table_name, columns):
        try:
            self.cur.execute('CREATE TABLE IF NOT EXISTS ' + table_name + ' (' + columns + ')')
        except Exception as e:
            print('Error:', e)
            sys.exit()

    def insert(self, table_name, columns, values):
        try:
            self.cur.execute('INSERT INTO ' + table_name + ' (' + columns + ') VALUES (' + values + ')')
        except Exception as e:
            print('Error:', e)
            sys.exit()

    def select(self, table_name, columns,
