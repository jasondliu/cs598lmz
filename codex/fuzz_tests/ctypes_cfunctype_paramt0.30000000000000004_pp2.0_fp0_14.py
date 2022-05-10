import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def c_callback(arg):
    print('callback called with arg:', arg)
    return arg * 2

c_callback = FUNTYPE(c_callback)

# test
print(c_callback(1))
</code>
Output:
<code>callback called with arg: 1
2
</code>

