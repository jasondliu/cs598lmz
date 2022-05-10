import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
@FUNTYPE
def fun2():
    return None

print(fun())
print(fun2())


class cF(FUNTYPE):
    def __call__(self,*args,**kwds):
        raise Exception("Hello!")

f=cF(lambda: 100)
print(f())
