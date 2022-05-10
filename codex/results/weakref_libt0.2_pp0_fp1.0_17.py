import weakref

from . import _base
from . import _util
from . import _compat
from . import _errors
from . import _types
from . import _cython

_logger = logging.getLogger(__name__)

_marker = object()


class _Cursor(_base.Cursor):
    """Cursor object for accessing the results of a database query.

    Cursors are not isolated, i.e. any changes done to the database by a
    cursor are immediately visible by other cursors or connections.
    """

    #: The :class:`~psycopg2.extensions.connection` using the cursor.
    connection = None

    #: The :class:`~psycopg2.extensions.connection` using the cursor.
    conn = None

    #: The :class:`~psycopg2.extensions.cursor` using the cursor.
    pgcursor = None

    #: The :class:`~psycopg2.extensions.cursor` using the cursor.
    cursor = None

    #: The :class
