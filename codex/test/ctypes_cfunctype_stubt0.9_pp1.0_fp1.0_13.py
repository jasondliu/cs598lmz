import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2, 3)
type(fun)

print(fun())

ttype = ctypes.py_object * 3
tnumtype = ctypes.c_int * 3
print(ttype)
type(tnumtype())
type(ttype())

num = ttype(1, 2, 3)
print(num)
print(type(fun())) # returns a tuple (1, 2, 3)
print(type(num)) # returns a py_object
print(type(ttype()))
num = ttype(*[1, 2, 3])
print(num)

#print(list(data2)[3])

#data3.__store__
