import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_db():
    db = sqlite3.connect('data.db')
    db.row_factory = sqlite3.Row
    return db

def create_tables(curs, sql_files):
    for sql_file in sql_files:
        with open(sql_file, 'r') as f:
            sql = f.read()
            curs.executescript(sql)

def create_views(curs, sql_files):
    for sql_file in sql_files:
        with open(sql_file, 'r') as f:
            sql = f.read()
            curs.executescript(sql)

def load_data(curs):
    with open('tables.yml', 'r') as stream:
        try:
            tables = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit(1)
    for table
