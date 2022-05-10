import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print x, y
    return x + y

mylib = ctypes.CDLL("./mylib.so")
mycallback = FUNTYPE(callback)
mylib.myfunc(mycallback)
</code>
It works, but I don't like it. I think that it is possible to get rid of the <code>ctypes</code> module and to create a Python function that is really a callback.
How can I do that?


A:

I'm not sure what you mean by "really a callback", but you can use the <code>ctypes</code> callback mechanism without using <code>ctypes</code> to load the library.
<code>import ctypes

def callback(x, y):
    print x, y
    return x + y

mylib = ctypes.CDLL("./mylib.so")
mycallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
