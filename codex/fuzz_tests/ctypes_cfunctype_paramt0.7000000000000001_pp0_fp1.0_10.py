import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test(i):
    print i
    return i*i

array = (FUNTYPE*2)()

array[0] = FUNTYPE(test)
array[0](3)
array[1] = FUNTYPE(test)
array[1](4)
</code>

