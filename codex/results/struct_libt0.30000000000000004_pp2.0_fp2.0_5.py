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

class _HeapType(_types.TypeType):
    """
    Internal base class for all heap types.
    """

    def __new__(cls, *args, **kwargs):
        if cls is _HeapType:
            raise TypeError('_HeapType is an abstract type')
        return _types.TypeType.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(_HeapType, self).__init__(*args, **
