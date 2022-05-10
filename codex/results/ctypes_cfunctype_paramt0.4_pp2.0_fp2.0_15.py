import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("hello from callback", x)
    return x

my_callback_type = FUNTYPE(my_callback)

mylib = ctypes.CDLL('mylib.so')
mylib.register_callback(my_callback_type)
mylib.call_callback()
</code>
Output:
<code>hello from callback 42
</code>

