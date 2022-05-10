import weakref

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import models

_engine = None
_session_factory = None
_session = None
_tables_created = False
_tables_refcount = 0


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine('sqlite:///:memory:', echo=False)
    return _engine


def get_session_factory():
    global _session_factory
    if _session_factory is None:
        _session_factory = sessionmaker(bind=get_engine())
    return _session_factory


def get_session():
    global _session
    if _session is None:
        _session = get_session_factory()()
    return _session


def create_tables():
    global _tables_created
    global _tables_refcount
    if not _tables_created:
        models.Base.metadata.create_all(get_engine())
        _t
