import threading
threading.stack_size(65536)


class Database:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.query('CREATE TABLE IF NOT EXISTS ' + table_name + '(' + columns + ')')
        self.conn.commit()

    def query(self, query, args=()):
        self.cursor.execute(query, args)
        self.conn.commit()
        return self.cursor

    def fetch(self, query, args=()):
        return self.query(query, args).fetchall()

    def fetch_one(self, query, args=()):
        return self.query(query, args).fetchone()

    def fetch_one_row(self, query, args=()):
        return self.query(query, args).fetchone()[0]

