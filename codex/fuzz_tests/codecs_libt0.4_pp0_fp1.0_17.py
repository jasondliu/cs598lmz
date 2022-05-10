import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_connection_string():
    # setup connection string
    # to do this, please define these environment variables first
    user_name = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')
    host = os.environ.get('MYSQL_HOST')
    db_name = os.environ.get('MYSQL_DB_NAME')
    db_port = os.environ.get('MYSQL_PORT')
    return 'mysql+pymysql://%s:%s@%s:%s/%s' % (user_name, password, host, db_port, db_name)

def get_connection():
    connection_string = get_connection_string()
    try:
        engine = create_engine(connection_string)
        connection = engine.connect()
        return connection
    except:
        print("Cannot connect to
