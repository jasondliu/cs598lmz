import weakref

from . import _base
from . import _util
from . import _compat
from . import _connection
from . import _cursor
from . import _proto
from . import _transaction
from . import _types
from . import _pool
from . import _errors
from . import _json


class Connection(_base.Connection):
    """A connection to a PostgreSQL database.

    The class :class:`Connection` encapsulates a database session.  You
    use this class to:

    - Establish a connection with the database.
    - Create cursors to execute queries and commands.
    - Commit and roll back transactions.
    - Close the connection.

    You can create a connection by passing a connection string to the
    :func:`~psycopg2.connect` function.

    .. code-block:: python

        >>> conn = psycopg2.connect("dbname=test user=postgres")

    The connection string can contain any of the following parameters:

    * *dbname* - the database name
    * *host* - the database host address (defaults to UNIX
