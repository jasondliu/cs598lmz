import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

# this is the function that will be called
def callback(fun):
    # this is the function that will be called
    def wrapper(*args, **kwargs):
        # call the function
        fun(*args, **kwargs)
        # call the callback
        callback.fun()
    return wrapper

@callback
def f():
    pass

callback.fun = fun

f()
</code>

