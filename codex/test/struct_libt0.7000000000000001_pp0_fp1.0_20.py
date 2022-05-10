import _struct
import _types
import _thread
import _errno
import _functools
import _io
import _heapq
import _weakref
import _warnings
import _collections

# pick up our own sysconfig
import sysconfig
_sysconfig = sysconfig.get_config_vars()

# Setup sys.implementation
sys.implementation = type('Implementation', (), {
    'name': 'micropython',
    'version': (sys.implementation.version.major, sys.implementation.version.minor, sys.implementation.version.micro, sys.implementation.version.releaselevel, sys.implementation.version.serial),
    'hexversion': sys.implementation.version.hex,
})

# Setup sys.flags
