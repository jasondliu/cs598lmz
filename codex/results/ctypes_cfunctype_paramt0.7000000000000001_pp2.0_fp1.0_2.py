import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def make_callback(func):
    "Make a Python callable that calls func"
    return FUNTYPE(func)

def callback(x, y):
    "A Python function that can be called from C"
    print(x, y)
    return x + y

cb = make_callback(callback)
print(cb)
cb(1, 2)
 

# callback = make_callback(callback)
# callback(1,2)
# <__main__.CFUNCTYPE object at 0x7f4e7b4c4e08>
# 1 2
# 3
