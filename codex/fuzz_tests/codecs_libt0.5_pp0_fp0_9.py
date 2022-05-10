import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class SQLDatabase:
    def __init__(self, config):
        self.config = config
        self.conn = MySQLdb.connect(host=self.config.database_host,
                                    user=self.config.database_username,
                                    passwd=self.config.database_password,
                                    db=self.config.database_name,
                                    charset='utf8mb4',
                                    use_unicode=True)
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute(self, query, args=None):
        if args is None:
            self.c.execute(query)
        else:
            self.c.execute(query, args)

        if query.lower().startswith('select'):
            return self.c.fetchall()
        else:
            self.conn.commit()

    def executemany(self,
