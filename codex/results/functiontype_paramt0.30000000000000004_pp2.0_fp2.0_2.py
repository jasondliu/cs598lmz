from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# ['__module__', '__qualname__', '__annotations__', '__kwdefaults__', '__defaults__', '__closure__', '__code__', '__globals__', '__dict__', '__doc__', '__name__', '__defaults__', '__code__', '__globals__', '__dict__']

# __code__
# __code__.co_argcount
# __code__.co_cellvars
# __code__.co_code
# __code__.co_consts
# __code__.co_filename
# __code__.co_firstlineno
# __code__.co_flags
# __code__.co_freevars
# __code__.co_kwonlyargcount
# __code__.co_lnotab
# __code__.co_name
# __code__.co_names
# __code__.co_nlocals
# __code__.co_stacksize
# __code
