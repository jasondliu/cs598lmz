import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

fun()

#fun.__name__
#fun.__doc__
#fun.__module__
#fun.__dict__
#fun.__closure__
#fun.__code__
#fun.__defaults__
#fun.__globals__
#fun.__dict__
#fun.__name__
#fun.__qualname__
#fun.__self__
#fun.__annotations__
#fun.__kwdefaults__

#fun.__code__.co_argcount
#fun.__code__.co_cellvars
#fun.__code__.co_code
#fun.__code__.co_consts
#fun.__code__.co_filename
#fun.__code__.co_firstlineno
#fun.__code__.co_flags
#fun.__code__.co_freevars
#fun.__code__.co_kwonlyargcount
#fun.__code__.co_lnotab
#fun.__code__.co_name
#fun.__
