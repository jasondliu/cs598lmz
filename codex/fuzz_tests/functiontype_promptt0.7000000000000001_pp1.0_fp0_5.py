import types
# Test types.FunctionType()
import __builtin__

from pypy.rlib.rarithmetic import intmask

from pypy.objspace.std.dictmultiobject import (
    W_DictMultiObject, dict_from_pairs, dict_iteration_value,
    dict_iteration_key, dict_iteration_item, dict_from_w_dict,
    dict_from_kwargs, W_DictMultiIterObject)
from pypy.objspace.std.dicttype import dict_typedef
from pypy.objspace.std.dictmultiobject import _never_equal_to_string
from pypy.objspace.std.multimethod import FailedToImplement
from pypy.objspace.std.multimethod import NoSuchAttrError
from pypy.objspace.std.model import registerimplementation, W_Object
from pypy.objspace.std.register_all import register_all
from pypy.objspace.std import stringtype
from pypy.objspace.std.stringobject import W_StringObject
from
