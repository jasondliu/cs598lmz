import codecs
codecs.register_error('surrogateescape', codecs.surrogateescape_error)

class Db:

    def __init__(self, dbname, verbose=False):
        self.dbname = dbname
        self.verbose = verbose
        self.connection = sqlite3.connect(self.dbname)

    def set_verbose(self, verbose):
        self.verbose = verbose

    def connect(self):
        self.connection = sqlite3.connect(self.dbname)

    def close(self):
        self.connection.close()

    def __execute_sql(self, sql, values):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(sql, values)
        self.connection.commit()
        self.close()

    #def __fetch_sql(self, sql, values):


    def __try_insert_or_update(self, table, id_name, id_value, value):
        self.connect()
        cursor = self.connection.cursor()
        sql = "SELECT
