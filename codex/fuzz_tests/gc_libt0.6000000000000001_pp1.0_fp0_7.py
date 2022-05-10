import gc, weakref

from pypy.module.cpyext.api import cpython_api, CANNOT_FAIL, Py_ssize_t, Py_buffer, Py_TPFLAGS_HAVE_WEAKREFS
from pypy.module.cpyext.pyobject import PyObject, PyObjectP, borrow_from
from pypy.module.cpyext.pyerrors import PyErr_BadInternalCall
from pypy.module.cpyext.pystate import PyThreadState
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import interp2app
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.buffer import Buffer
from rpython.rlib.objectmodel import we_are_translated
from rpython.rlib.rarithmetic import ovfcheck
from rpython.rlib.unroll import unrolling_iterable
from rpython.rtyper.lltypesystem
