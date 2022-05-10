import _struct
import _syscall
import _termios
import _thread
import _time
import _unix
import _weakref
import _zlib
import _zmq

import _ssl
try:
    import _hashlib
except ImportError:
    # hashlib is new in 2.5
    pass

try:
    import _bz2
except ImportError:
    # bz2 is new in 2.3
    pass

try:
    import _ctypes
except ImportError:
    # ctypes is new in 2.5
    pass

try:
    import _elementtree
except ImportError:
    # elementtree is new in 2.5
    pass

try:
    import _hotshot
except ImportError:
    # hotshot is new in 2.3
    pass

try:
    import _json
except ImportError:
    # json is new in 2.6
    pass

try:
    import _lsprof
except ImportError:
    # lsprof is new in 2.5
    pass

