import _struct
import _sys
import _sysconfig
import _thread
import _threading_local
import _time
import _traceback
import _types
import _weakref
import _warnings
import _weakrefset
import _functools
import _operator
import _collections

from _functools import partial as _partial
from _weakref import proxy as _proxy
from _collections import deque as _deque
from _collections import UserDict as _UserDict
from _collections import UserList as _UserList
from _collections import UserString as _UserString

# Support for dynamic loading of C extension modules
# -------------------------------------------------
#
# In order to keep the startup time of Python interpreter low, we don't
# want to load the whole CPython module. So we load only the parts needed
# for bootstrapping the interpreter process.
#
# The CPython module is a dynamically loadable module. In order to be able
# to load it, we need to provide an implementation of the _imp module.
#
# The _imp module is the only module that is implemented in C.
