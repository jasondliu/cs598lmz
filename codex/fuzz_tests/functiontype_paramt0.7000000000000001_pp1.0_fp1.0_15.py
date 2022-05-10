from types import FunctionType
list(FunctionType(obj).__globals__)

list(FunctionType(obj).__code__.co_consts)

list(FunctionType(obj).__code__.co_names)

list(FunctionType(obj).__code__.co_varnames)

FunctionType(obj).__code__.co_argcount

FunctionType(obj).__code__.co_flags

## 不可变类型
# 1. 实例不可变，类可变
# 2. 所有属性都是私有的, 只能通过特殊方法访问
# 3. 实例不可改变，可以删除实例
import types
def Frozen(cls):
    if type(cls) is types.FunctionType:
        cls = cls()
    for n, v in cls.__
