import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get():
    EMAIL = os.environ.get('AXA_EMAIL', default)
    PW = os.environ.get('AXA_PW', default)
    HOST = os.environ.get('AXA_HOST', default)
    DBNAME = os.environ.get('AXA_DB', default)
    charset = os.environ.get('AXA_CHARSET', default)
    assertion = os.environ.get('AXA_ASSERTION', default)
    if charset == default:
        charset = 'utf8mb4'

    db_connection_args = {'host': HOST, 'user': EMAIL, 'password': PW, 'database': DBNAME, 'charset': charset}

    return db_connection_args
