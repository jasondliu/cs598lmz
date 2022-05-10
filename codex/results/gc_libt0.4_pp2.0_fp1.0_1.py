import gc, weakref
from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import unwrap_spec, WrappedDefault
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.buffer import Buffer
from pypy.interpreter.typedef import TypeDef, interp_attrproperty
from pypy.interpreter.gateway import interp2app, unwrap_spec
from rpython.rlib import rgc
from rpython.rlib.rweakref import RWeakKeyDictionary
from rpython.rlib.objectmodel import we_are_translated
from rpython.rlib.rarithmetic import intmask


class W_PyCTypesObject(W_Root):
    _immutable_fields_ = ['_ctype', '_value']
    _attrs_ = ['_ctype', '_value']
    _value = None

    def __init__(self, space, ctype, value
