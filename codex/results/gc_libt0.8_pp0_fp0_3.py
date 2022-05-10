import gc, weakref, ctypes

import pypy.rlib.rweakref
import pypy.rlib.rarithmetic
import pypy.rlib.objectmodel as objectmodel

from pypy.interpreter.error import OperationError
from pypy.interpreter.baseobjspace import W_Root, Wrappable
from pypy.interpreter.gateway import ObjSpace, interp2app
from pypy.interpreter.typedef import TypeDef
from pypy.interpreter.typedef import GetSetProperty
from pypy.objspace.std.dictobject import W_DictMultiObject
from pypy.objspace.std.listobject import W_ListObject
from pypy.objspace.std.tupleobject import W_TupleObject
from pypy.objspace.std.model import registerimplementation, W_Object
from pypy.objspace.std.register_all import register_all

# ____________________________________________________________

# XXX: Should have a single dict containing all this information
# and an object that know how
