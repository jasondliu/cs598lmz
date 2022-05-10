from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__module__', '__qualname__', '__annotations__', '__kwdefaults__', '__closure__', '__code__', '__defaults__', '__globals__', '__dict__', '__doc__', '__name__', '__self__', '__get__', '__func__', '__repr__', '__hash__', '__str__', '__call__', '__dir__', '__delattr__', '__setattr__', '__eq__', '__ne__', '__lt__', '__le__', '__gt__', '__ge__', '__new__', '__init_subclass__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

# 从上面的结果可以看
