import weakref

_SCOPED_SESSION = threading.local()


def get_scoped_session():
    # type: () -> scoped_session
    if getattr(_SCOPED_SESSION, 'scoped_session', None) is None:
        _SCOPED_SESSION.scoped_session = scoped_session(
            sessionmaker(
                bind=create_engine(settings.DATABASE_URL, echo=settings.SQLALCHEMY_ECHO),
                lazy=True),
            weak_identity_map=True)
    return _SCOPED_SESSION.scoped_session


@event.listens_for(Session, 'after_transaction_end')
def session_after_transaction_end(session, transaction):
    session.remove()


@event.listens_for(Session, 'after_soft_rollback')
def session_after_soft_rollback(session, previous_transaction, new_transaction):
    session.remove()


@contextlib.contextmanager
def session_scope():
    # type
