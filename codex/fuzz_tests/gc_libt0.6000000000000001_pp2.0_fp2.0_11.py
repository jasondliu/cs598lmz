import gc, weakref
from weakref import WeakValueDictionary
from weakref import WeakKeyDictionary

from pypy.interpreter import gateway
from pypy.interpreter.typedef import TypeDef
from pypy.interpreter.gateway import ObjSpace, W_Root, NoneNotWrapped
from pypy.interpreter.baseobjspace import W_Root, ObjSpace
from pypy.interpreter.error import oefmt
from pypy.interpreter.typedef import GetSetProperty
from pypy.objspace.std.dictmultiobject import (
    W_DictMultiObject, W_DictMultiIterObject, EMPTY_DICT)
from pypy.objspace.std.dictmultiobject import setitem__DictMulti_ANY
from pypy.objspace.std.dictmultiobject import wrapvalue
from pypy.objspace.std.dictmultiobject import unwrapvalue
from pypy.objspace.std.listobject import W_ListObject
from pypy.objspace.std.listobject import W_ListObject
