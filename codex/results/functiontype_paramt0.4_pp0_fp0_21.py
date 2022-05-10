from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_varnames)

# ['__doc__', '__module__', '__qualname__', '__defaults__', '__kwdefaults__', '__annotations__', '__code__', '__globals__', '__closure__', '__dict__', '__weakref__', '__text_signature__', '__name__', '__qualname__', '__self__', '__func__', '__self_class__', '__self_class_instance__', '__self_last_resort__', '__next_in_mro__', '__get__', '__set__', '__delete__', '__isabstractmethod__', '__func__', '__self__', '__module__', '__defaults__', '__kwdefaults__', '__annotations__', '__dict__', '__weakref__', '__text_signature__', '__slots__', '__objclass__', '__args__', '__next_in_mro__', '__get
