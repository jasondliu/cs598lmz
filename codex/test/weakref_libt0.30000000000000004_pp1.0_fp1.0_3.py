import weakref

from . import _base
from . import _util
from . import _errors

from . import _compat as _c

__all__ = ['Connection']

class Connection(_base.Connection):
    """Connection to a PostgreSQL database"""

