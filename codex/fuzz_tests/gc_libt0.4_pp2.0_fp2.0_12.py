import gc, weakref
import sys
import time
import traceback
import types

from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import unwrap_spec, WrappedDefault
from pypy.interpreter.typedef import TypeDef, GetSetProperty, interp_attrproperty
from pypy.interpreter.typedef import interp_attrproperty_w
from pypy.interpreter.baseobjspace import W_Root, ObjSpace, Wrappable, \
     Arguments
from pypy.interpreter.buffer import Buffer
from pypy.interpreter.typedef import make_weakref_descr
from pypy.interpreter.typedef import interp_attrproperty_w
from pypy.interpreter.gateway import interp2app, unwrap_spec
from rpython.rlib import rgc
from rpython.rlib.objectmodel import we_are_translated
from rpython.rlib.rstring import StringBuilder
from rpython.rlib.
