import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun")
    return "funreturn"

def fun1(x,y):
    return x+y

def fun2(x,y):
    return x*y

functype = FUNTYPE(fun1)
print(functype(1,2))
functype = FUNTYPE(fun2)
print(functype(1,2))

functype = FUNTYPE(fun)
print(functype())
