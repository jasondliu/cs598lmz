import weakref

from . import _ffi
from . import _lib
from . import _util
from . import _winreg
from . import _winreg_unicode

from . import _winreg_unicode

_ffi.cdef('''
    typedef struct {
        ...;
    } PyHKEY;
''')

_PyHKEY = _ffi.typeof('PyHKEY')

_PyHKEY_p = _ffi.typeof('PyHKEY *')

_PyHKEY_p_p = _ffi.typeof('PyHKEY **')

_PyHKEY_p_p_p = _ffi.typeof('PyHKEY ***')
