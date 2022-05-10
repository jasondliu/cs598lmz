import _struct
import _string
import _sys
import _thread
import _time
import _types
import _warnings
import _weakref

# Import the builtin modules.
import __builtin__
import exceptions

# Import the warnings module, but do not override the built-in one if we are
# running in optimized mode.
import warnings as _warnings

# Set up the built-in modules.
# sys.modules is altered in place so that some other modules can see a
# partially-completed sys.modules and act on that knowledge (e.g. email.utils
# uses sys.modules to import several modules).
_sys.modules["__builtin__"] = __builtin__
_sys.modules["exceptions"] = exceptions
_sys.modules["_warnings"] = _warnings

# Some modules need to make early references to other modules.
import _codecs
import _weakref
import _functools
import _operator
import _collections
import _abc
import _io
import _heapq
import _locale
import _random
import _socket
import _s
