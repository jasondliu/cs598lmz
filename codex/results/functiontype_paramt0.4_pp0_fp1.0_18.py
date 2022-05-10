from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f') for x in range(10))

# __code__
# __defaults__
# __closure__
# __globals__
# __dict__
# __name__
# __qualname__
# __module__
# __annotations__
# __kwdefaults__
# __text_signature__

# def f(x: int, y: int = 0) -> int:
#     return x + y

# f.__code__
# f.__code__.co_varnames
# f.__code__.co_argcount
# f.__code__.co_kwonlyargcount
# f.__code__.co_nlocals
# f.__code__.co_stacksize
# f.__code__.co_flags
# f.__code__.co_consts
# f.__code__.co_names
# f.__code__.co_varnames
# f.__code__.co_freevars
# f.__code__.co_cellv
