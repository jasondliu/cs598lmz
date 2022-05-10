import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "hello"

print(fun())
print(fun2())
print(fun2.__code__)
print(fun2.__code__.co_code)
print(fun2.__code__.co_consts)
print(fun2.__code__.co_names)
print(fun2.__code__.co_varnames)
print(fun2.__code__.co_freevars)
print(fun2.__code__.co_cellvars)
print(fun2.__code__.co_filename)
print(fun2.__code__.co_name)
print(fun2.__code__.co_firstlineno)
print(fun2.__code__.co_lnotab)
print(fun2.__code__.co_argcount)
print(fun2.__code__.co_kwonlyargcount)
print(fun2.__code__.co_nlocals)
print(fun2.__code__.co_stacksize)

