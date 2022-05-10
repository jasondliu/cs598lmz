import gc, weakref

import py
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import interp2app, unwrap_spec
from pypy.interpreter.typedef import TypeDef, GetSetProperty
from pypy.interpreter.typedef import interp_attrproperty
from pypy.interpreter.typedef import interp_attrproperty_w
from pypy.interpreter.typedef import interp_attrproperty_d
from pypy.module.__builtin__.abstractinst import abstract_issubclass
from pypy.module.__builtin__.abstractinst import abstract_isinstance
from pypy.module.__builtin__.abstractinst import abstract_getclass
from pypy.module.__builtin__.abstractinst import class_is_abstract
from pypy.module._weakref.interp_weakref import W_Weakref
from pypy.objspace.
