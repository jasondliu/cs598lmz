import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print('callback called with %d and %d' % (x, y))
    return x + y

cb = FUNTYPE(callback)

# call the function
print(lib.callback_func(cb))

# call the function again
print(lib.callback_func(cb))

# call the function with a different callback
def callback_2(x, y):
    print('callback_2 called with %d and %d' % (x, y))
    return x * y

cb2 = FUNTYPE(callback_2)
print(lib.callback_func(cb2))

# call the function with a different callback
def callback_3(x, y):
    print('callback_3 called with %d and %d' % (x, y))
    return x * y

cb3 = FUNTYPE(callback_3)
print(lib.callback_func(cb3))

# call the function with a different callback
def callback_
