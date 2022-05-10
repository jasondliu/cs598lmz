import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def make_callback(func):
    return FUNTYPE(func)

def callback(x, y):
    print("x:", x, "y:", y)
    return x + y

if __name__ == "__main__":
    callback_func = make_callback(callback)
    print(callback_func(2, 3))
</code>
Output:
<code>x: 2 y: 3
5
</code>

