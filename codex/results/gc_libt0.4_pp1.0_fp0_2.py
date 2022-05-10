import gc, weakref
from pypy.interpreter.baseobjspace import Wrappable
from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import interp2app, unwrap_spec
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.typedef import interp_attrproperty
from pypy.module._weakref.interp_weakref import W_Weakref, wrap_weakref
from pypy.module._weakref.interp_weakref import unwrap_weakref
from rpython.rlib import rgc
from rpython.rlib.debug import ll_assert
from rpython.rlib.objectmodel import we_are_translated, compute_unique_id
from rpython.rlib.rarithmetic import intmask, r_uint
from rpython.rlib.rweaklist import WeakList
from rpython.rlib.signature import signature
from rpython.rtyper.lltypesystem import lltype, rffi
from r
