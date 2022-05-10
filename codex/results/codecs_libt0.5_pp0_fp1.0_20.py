import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def get_db_engine():
    db_engine = create_engine(
        'mysql+pymysql://root:@localhost:3306/test',
        encoding='utf8mb4',
        pool_recycle=3600,
        pool_size=20,
        max_overflow=0,
        pool_pre_ping=True)
    return db_engine

def get_db_session(db_engine):
    Session = sessionmaker(bind=db_engine)
    session = Session()
    return session

def get_db_session_transaction(db_engine):
    Session = sessionmaker(bind=db_engine)
    session = Session()
    session.begin(subtransactions=True)
    return session

def get_db_session_transaction_autocommit(db_engine):
    Session = sessionmaker(bind=db_engine)
    session = Session()
    session.begin(subtransactions
