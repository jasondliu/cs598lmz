import types
types.TypeType = type

import copy_reg
import copy
from types import MethodType


def copy_method(method):
    return type(method)(method.im_func, copy.copy(method.im_self), method.im_class)

copy_reg.pickle(MethodType, copy_method)


def func2method(func, self, cls):
    if func.__name__ == '__init__':
        return func
    return types.MethodType(func, self, cls)


copy_reg.pickle(types.FunctionType, func2method)
