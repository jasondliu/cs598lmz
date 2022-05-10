import weakref

from . import _base
from . import _util
from . import _compat
from . import _errors
from . import _types
from . import _protocol
from . import _cython

from . import _cython

if _cython.compiled:
    from . import _cython_impl as _impl
else:
    from . import _python_impl as _impl


def _get_connection(connection):
    if connection is None:
        connection = _base.get_connection()
    elif isinstance(connection, _base.Connection):
        connection = connection
    elif isinstance(connection, _base.Session):
        connection = connection.connection
    else:
        raise TypeError("connection must be a Connection or Session")
    return connection


def _get_session(session):
    if session is None:
        session = _base.get_session()
    elif isinstance(session, _base.Session):
        session = session
    elif isinstance(session, _base.Connection):
        session = session.session

