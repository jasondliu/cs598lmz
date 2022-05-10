import weakref
import traceback

from sqlalchemy.orm.session import Session as SQLAlchemySession

class Session(object):
    """
    SQLAlchemy session handler
    """

    _engine = None
    _initialized = False

    def __init__(self, settings, prefix='sqlalchemy.'):
        if not Session._initialized:
            Session._engine = engine_from_config(settings, prefix)
            Session._initialized = True
        self.session = scoped_session(sessionmaker(bind=Session._engine))

    def remove(self):
        self.session.remove()

class SQLAlchemyRequest(object):
    """
    SQLAlchemy request handler
    """

    @reify
    def session(self):
        """
        Return a SQLAlchemy session on a per-request basis
        """
        session = getattr(self.request, '_sa_session', None)
        if session is None:
            db_session = getattr(self.request, 'db_session', None)
