from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# 使用inspect.getmembers()函数获取对象的成员
import inspect
inspect.getmembers(FunctionType(lambda: None))

# [('__call__', <method-wrapper '__call__' of
