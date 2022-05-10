import weakref

from . import _util
from . import _compat
from . import _context
from . import _config
from . import _connection
from . import _cursor
from . import _exceptions
from . import _pool
from . import _transaction
from . import _types
from . import _version

_logger = _util.get_logger(__name__)


class Connection(_connection.Connection):
    """Connection object."""

    def __init__(self, *args, **kwargs):
        """Constructor."""
        super(Connection, self).__init__(*args, **kwargs)

        self._transaction = _transaction.Transaction(self)
        self._transaction.__enter__()

    def __enter__(self):
        """Enter the runtime context related to this object."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object."""
        self.close()

    def __del__(self):
        """Destructor."
