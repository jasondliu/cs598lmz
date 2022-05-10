from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda: (yield from range(10))).gi_yieldfrom)

# __code__
# __defaults__
# __globals__
# __closure__
# __name__
# __qualname__

# __annotations__
# __kwdefaults__

# __dict__
# __module__
# __text_signature__
# __get__
# __set__
# __delete__
# __slots__
# __init_subclass__
# __class_getitem__
# __prepare__
# __instancecheck__
# __subclasscheck__
# __subclasshook__
# __init_subclass__
# __new__
# __init__
# __call__
# __getattr__
# __getattribute__
# __setattr__
# __delattr__
# __dir__
# __get__

