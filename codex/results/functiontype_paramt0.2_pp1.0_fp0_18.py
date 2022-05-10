from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__builtins__', '__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__kwdefaults__', '__globals__', '__closure__', '__code__', '__defaults__', '__kwonlyargs__', '__annotations__', '__dict__', '__weakref__', '__module__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '__subclasses__', '__prepare__', '__instancecheck__', '__subclass
