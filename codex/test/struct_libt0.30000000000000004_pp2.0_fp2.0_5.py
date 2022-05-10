import _struct

from . import _util
from . import _compat
from . import _constants
from . import _errors
from . import _types
from . import _lib
from . import _ffi

_ffi.cdef('''
    typedef struct {
        PyObject_HEAD
        PyObject *dict;
        PyObject *weaklist;
        PyObject *name;
        PyObject *qualname;
        PyObject *bases;
        PyObject *mro;
    } PyHeapTypeObject;
''')

