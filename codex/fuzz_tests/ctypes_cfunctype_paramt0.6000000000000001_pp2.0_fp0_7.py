import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))

def func1(i):
    print 'func1', i.contents.value

def func2(i):
    print 'func2', i.contents.value

f1 = FUNTYPE(func1)
f2 = FUNTYPE(func2)

arr = (FUNTYPE * 2)()
arr[0] = f1
arr[1] = f2

i = ctypes.c_int(10)
arr[0](i)
arr[1](i)
</code>

