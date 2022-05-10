import weakref

from . import _base
from . import _util
from . import _compat

from . import _errors
from . import _types
from . import _protocol
from . import _cython

from . import _connection
from . import _cursor
from . import _pool
from . import _transaction

from . import _lob
from . import _nchar
from . import _nclob
from . import _cx_oracle_objects

from . import _version

#-----------------------------------------------------------------------------
# Module globals
#-----------------------------------------------------------------------------

#: The version of cx_Oracle as a tuple of ints
version = _version.version

#: The version of cx_Oracle as a string
versionString = _version.versionString

#: The version of the Oracle client library as a tuple of ints
clientVersion = _version.clientVersion

#: The version of the Oracle client library as a string
clientVersionString = _version.clientVersionString

#: The version of the Oracle DB API specification supported by cx_Oracle
apilevel = _version.apilevel
