import _struct
import _traceback
import _types
import _warnings
import _weakref

# These modules are not available in restricted mode.
if not _os.W_OK & _os.access("", _os.W_OK):
    _sys.modules['_dummy_thread'] = _thread
    _sys.modules['_socket'] = _socket
    _sys.modules['array'] = _array
    _sys.modules['audioop'] = _audioop
    _sys.modules['binascii'] = _binascii
    _sys.modules['cmath'] = _cmath
    _sys.modules['errno'] = _errno
    _sys.modules['fcntl'] = _fcntl
    _sys.modules['future_builtins'] = _future_builtins
    _sys.modules['grp'] = _grp
    _sys.modules['itertools'] = _itertools
    _sys.modules['math'] = _math
    _sys.modules['mmap'] = _mmap
    _sys.modules['parser'] =
