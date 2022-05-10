import _struct
import _string
import _math
from _weakref import proxy
from array import array
_id = id


import math


__all__ = [
    'OSError', 'error', 'environ', 'listdir', 'remove', 'rename', 'tmpfile',
    'tmpnam', 'utsname', 'popen', 'popen2', 'popen3', 'popen4', 'system',
    'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'startfile', 'exit',
    'helper', 'abort',
    ]
del _sys
del sys
del _struct
del _string
del _math
del array
del _id


class OSError(EnvironmentError):
    __qualname__ = 'OSError'

    def __reduce__(self):
        return (OSError, (self.errno, self.strerror, self.filename))

    def __init__(self, *args):
        import _thread
        try:
            t = _thread.get_ident()
        except AttributeError:
