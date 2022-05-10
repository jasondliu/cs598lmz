import gc, weakref

from pypy.interpreter.error import OperationError
from pypy.interpreter.gateway import ObjSpace
from pypy.interpreter.typedef import TypeDef
from pypy.interpreter.baseobjspace import W_Root
from pypy.interpreter.typedef import interp_attrproperty
from pypy.interpreter.gateway import interp2app
from pypy.interpreter.gateway import unwrap_spec
from pypy.interpreter.argument import Arguments
from pypy.interpreter.typedef import GetSetProperty
from pypy.interpreter.typedef import descr_get_dict
from pypy.interpreter.typedef import descr_set_dict
from pypy.interpreter.typedef import descr_del_dict
from pypy.interpreter.typedef import make_weakref_descr
from pypy.interpreter.typedef import interp_attrproperty_w
from pypy.
