import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class DAL(object):
    def __init__(self, filename='data.sqlite'):
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def execute(self, sql, params=None):
        if params:
            self.c.execute(sql, params)
        else:
            self.c.execute(sql)

    def executemany(self, sql, params):
        self.c.executemany(sql, params)

    def fetchone(self):
        return self.c.fetchone()

    def fetchall(self):
        return self.c.fetchall()

    def fetch_rows(self, sql, params=
