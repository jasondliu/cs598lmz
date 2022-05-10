import _struct

from pypy.interpreter import argument
from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import (
    unwrap_spec, WrappedDefault, interp2app, interpindirect2app)
from pypy.interpreter.typedef import TypeDef, GetSetProperty, make_weakref_descr
