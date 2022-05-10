import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))

def callback(x, y):
    y[0] = x[0] * x[0]

callback_func = FUNTYPE(callback)

# create an array of 1 element
x_array = ctypes.c_double * 1
y_array = ctypes.c_double * 1
x = x_array(ctypes.c_double(10.0))
y = y_array(ctypes.c_double(0.0))

# call the function
callback_func.restype = ctypes.c_double
callback_func.argtypes = [x_array, y_array]
callback_func(x, y)
print y[0]
</code>
This works, but I don't like the way it works (i.e., the way it's done... there's got to be a cleaner way).
Is there a better way to do this?


A:

<code>ctypes</code> can create
