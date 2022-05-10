import gc, weakref

from . import _core
from . import _util
from . import _types
from . import _data
from . import _error
from . import _cursor
from . import _connection
from . import _transaction
from . import _statement
from . import _pool
from . import _result
from . import _lob
from . import _datetime
from . import _interval
from . import _numbers
from . import _binary
from . import _external
from . import _internal
from . import _version

from . import _mock

from . import _fix

from . import _threaded

from . import _version

from . import _fix

from . import _mock

#
# This is the main cx_Oracle namespace.
#

#
# Version information.
#
version = _version.version
versionTuple = _version.versionTuple

#
# Exceptions.
#
DatabaseError = _error.DatabaseError
InterfaceError = _error.InterfaceError
InternalError = _error.InternalError
OperationalError = _error.
