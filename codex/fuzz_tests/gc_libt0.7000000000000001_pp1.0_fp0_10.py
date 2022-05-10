import gc, weakref
from pypy.module.cpyext.api import (
    cpython_api, slot_function, PyObject, Py_ssize_t, Py_ssize_tP, Py_TPFLAGS_HAVE_VERSION_TAG,
    Py_TPFLAGS_VALID_VERSION_TAG, cpython_struct, bootstrap_function, Py_bufferP,
    CONST_STRING, CANNOT_FAIL, PyObjectFields,
    Py_ssize_t, build_type_checkers, generic_cpy_call, build_type_checkers)
from pypy.module.cpyext.pyobject import (
    PyObject, PyObjectP, Py_DecRef, make_ref, from_ref, decref, track_reference,
    make_typedescr, get_typedescr)
from rpython.rlib.rgc import (
    resizable_list_supporting_raw_ptr, resizable_list_supporting_raw_ptr_for_item)
from rpython.rlib.objectmodel import keepalive_until
