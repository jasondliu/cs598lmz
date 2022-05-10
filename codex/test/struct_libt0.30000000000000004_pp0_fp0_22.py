import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# The following modules are written in Python.
# They have to be loaded in a special way in order to not trigger
# the automatic import hook (which would try to load them as builtin
# modules).

import _codecs
import _collections
import _functools
import _io
import _locale
import _operator
import _signal
import _sre
import _stat
import _string
import _symtable
import _thread
import _tracemalloc
import _warnings

# The _weakref module is implemented in Python, but the weakref
# objects are builtin.
import _weakref
import _weakrefset

# These modules are optional and may not be present
# (e.g. when not configured with --with-threads)

try:
    import _thread
except ImportError:
    pass

try:
    import _multiprocessing
except ImportError:
    pass

