import gc, weakref, sys
from rpython.rlib import rgc
from rpython.rlib.objectmodel import we_are_translated

from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import unwrap_spec, interp2app, unwrap_spec
from pypy.interpreter.typedef import TypeDef, GetSetProperty, make_weakref_descr
from pypy.interpreter.baseobjspace import Wrappable
from pypy.interpreter.typedef import TypeDef, interp_attrproperty
from pypy.interpreter.typedef import interp_attrproperty_w
from rpython.rlib.objectmodel import compute_hash, compute_unique_id
from rpython.rlib.rarithmetic import intmask, r_uint, r_longlong
from rpython.rlib.rweakref import RWeakKeyDictionary, RWeakValueDictionary
from rpython.rlib import jit
from rpython.rlib.objectmodel import compute_hash
from r
