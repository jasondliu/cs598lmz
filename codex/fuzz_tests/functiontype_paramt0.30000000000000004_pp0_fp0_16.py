from types import FunctionType
list(FunctionType(lambda: 0, {}).__code__.co_varnames)

# ['__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__kwdefaults__', '__globals__', '__code__', '__defaults__', '__closure__', '__dict__', '__weakref__', '__module__', '__hash__', '__eq__', '__ne__', '__lt__', '__le__', '__gt__', '__ge__', '__new__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '__get__', '__set__', '__delete__', '__prepare__', '__instancecheck__', '__subclasscheck__', '__call__', '__getattribute__', '__setattr__', '__delattr__', '
