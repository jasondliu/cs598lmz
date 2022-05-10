import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return b"hello"

print(fun())
print(fun.__name__)
print(fun.__doc__)
print(fun.__closure__)
print(fun.__code__)
print(fun.__defaults__)
print(fun.__dict__)
print(fun.__globals__)
print(fun.__module__)
print(fun.__name__)
print(fun.__qualname__)
print(fun.__annotations__)
print(fun.__kwdefaults__)

#cannot set attributes
#fun.__name__ = "new name"
#print(fun.__name__)


print(fun.__closure__)
print(fun.__code__)
print(fun.__defaults__)
print(fun.__dict__)
print(fun.__globals__)
print(fun.__module__)
print(fun.__name__)
print(fun.__qualname__)
print(fun.__annotations__)
print(fun.__
