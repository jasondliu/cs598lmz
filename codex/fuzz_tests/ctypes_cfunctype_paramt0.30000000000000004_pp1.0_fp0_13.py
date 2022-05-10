import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python callback", a, b
    return a + b

my_callback_func = FUNTYPE(my_callback)

lib.set_callback(my_callback_func)
</code>
The above code works fine, but I would like to do something like this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python callback", a, b
    return a + b

lib.set_callback(FUNTYPE(my_callback))
</code>
But this gives me the error:
<code>TypeError: in method 'set_callback', argument 1 of type 'int (*)(int, int)'
</code>
Is there a way to do this?


A:

<code>ctypes.CFUNCTYPE</code> is
