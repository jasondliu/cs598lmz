import weakref

from . import _base
from . import _common
from . import _compat
from . import _constants
from . import _errors
from . import _util
from . import _vendor
from . import _version

try:
    from typing import Any
    from typing import Dict
    from typing import List
    from typing import Optional
    from typing import Tuple
    from typing import Type
    from typing import Union
except ImportError:
    pass

__all__ = [
    "Cursor",
    "CursorType",
    "MySQLCursor",
    "MySQLCursorBuffered",
    "MySQLCursorBufferedRaw",
    "MySQLCursorDict",
    "MySQLCursorRaw",
    "MySQLCursorPrepared",
]


class CursorType(_base.CursorType):
    """MySQL cursor types."""

    _types = {
        "plain": _constants.CURSOR_TYPE_NO_CURSOR,
        "buffered": _constants.
