import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
print(fun.__name__)
print(fun.__code__.co_argcount)
print(fun.__code__.co_varnames)
print(fun.__code__.co_filename)
print(fun.__code__.co_name)
print(fun.__code__.co_flags)
print(fun.__code__.co_consts)
print(fun.__code__.co_firstlineno)
print(fun.__code__.co_lnotab)
print(fun.__code__.co_stacksize)
print(fun.__code__.co_freevars)
print(fun.__code__.co_cellvars)

#import dis
#dis.dis(fun)

#print(fun.__code__.co_code)


#print(fun.__code__.co_code)
#print(fun.__code__.co_code)
#print(fun.__code__.co_code)
#print(fun.__
