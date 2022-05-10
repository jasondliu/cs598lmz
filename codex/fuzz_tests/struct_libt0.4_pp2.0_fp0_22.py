import _struct
import sys

from . import _common
from . import _compat
from . import _constants
from . import _errors
from . import _ffi
from . import _lib
from . import _util

_ffi.cdef(
    """
    typedef struct {
        PyObject_HEAD
        PyObject *dict;
        PyObject *weakreflist;
        PyObject *name;
        PyObject *qualname;
        PyObject *doc;
        PyObject *module;
        PyObject *dictoffset;
        PyObject *dict;
        PyObject *weakreflist;
        PyObject *tp_dict;
        PyObject *tp_weaklist;
        PyObject *tp_mro;
        PyObject *tp_cache;
        PyObject *tp_subclasses;
        PyObject *tp_weaklistoffset;
        PyObject *tp_base;
        PyObject *tp_dictoffset;
        PyObject *tp_bases;
        PyObject *tp_mro;
        PyObject *tp_cache;
        PyObject
