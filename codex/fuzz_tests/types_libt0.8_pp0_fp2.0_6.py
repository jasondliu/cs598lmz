import types
types.ModuleType( "psycopg2._psycopg" )
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)


class PostgreSQL(SQL):
    def __init__(self, dbname, user, password, host='localhost', port=5432, *args, **kwargs):
        self.config = {
                    'dbname': dbname,
                    'user': user,
                    'password': password,
                    'host': host,
                    'port': port,
                }
        SQL.__init__(self, *args, **kwargs)

    def _connect(self):
        self.db = psycopg2.connect(
            database=self.config['dbname'],
            user=self.config['user'],
            password=self.config['password'],
            host=self.config['host'],
            port=self.config['port'],
            cursor_factory=psycopg2.extras.DictCursor

