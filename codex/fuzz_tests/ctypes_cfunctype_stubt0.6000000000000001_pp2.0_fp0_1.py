import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2(a,b):
    return a*b

@FUNTYPE
def fun3(a,b):
    return [a,b]

@FUNTYPE
def fun4(a):
    return a

@FUNTYPE
def fun5(a):
    return [a]

@FUNTYPE
def fun6(a):
    return [a,a]

print(fun())
print(fun2(1,2))
print(fun3(1,2))
print(fun4(1))
print(fun5(1))
print(fun6(1))
print(fun())
print(fun2(1,2))
print(fun3(1,2))
print(fun4(1))
print(fun5(1))
print(fun6(1))
print(fun())
print(fun2(1,2))
print(fun3(1,2))
print(fun4(1))
print(fun5(1))
print(fun6(1))
print(fun())
print(
