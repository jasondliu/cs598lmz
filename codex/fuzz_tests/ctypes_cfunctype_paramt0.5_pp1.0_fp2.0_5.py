import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(i):
    print("func", i)
    return i

f = FUNTYPE(func)
f(1)

def func2(i):
    print("func2", i)
    return i

f2 = FUNTYPE(func2)
f2(2)

f = FUNTYPE(func)
f2(3)
</code>
Output:
<code>func 1
func2 2
func 2
</code>

