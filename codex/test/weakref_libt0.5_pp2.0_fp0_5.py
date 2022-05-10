import weakref

from . import _common
from . import _compat
from . import _constants
from . import _errors
from . import _util
from . import _wrapper

__all__ = [
    'Cursor',
]


class Cursor(_wrapper.Wrapper):
    """
    Execute SQL and retrieve results.

    This class is not constructed directly by the user. Instead, it is
    constructed by :class:`~.Connection`.

    The :class:`~.Cursor` class is used to execute SQL statements and retrieve
    results.

    A :class:`~.Cursor` object has an execution context that is contained in the
    :class:`~.Connection` object that created it.

    .. seealso::

        `Cursor Objects`_ - DB-API 2.0 specification.

    """
    __slots__ = ()

    def __init__(self, connection):
        super(Cursor, self).__init__()
        self._setup(connection)

