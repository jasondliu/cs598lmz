import gc, weakref
from weakref import WeakKeyDictionary, WeakSet

from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import interp2app, unwrap_spec, WrappedDefault
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.baseobjspace import W_Root, ObjSpace
from pypy.interpreter.argument import Arguments
from pypy.interpreter.typedef import interp_attrproperty
from pypy.module._weakref.interp_weakref import W_Weakref, W_CallableProxy
from pypy.rlib.objectmodel import we_are_translated, specialize
from pypy.rlib.debug import make_sure_not_resized
from pypy.rlib.rarithmetic import intmask, r_uint
from pypy.rlib.rweaklist import AbstractWeakList, WeakList, WeakListIterator
from pypy.rlib.rweakref import AbstractReference, CallbackReference
from p
