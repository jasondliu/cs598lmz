import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)

def callback(result, error):
    print "callback had result %s and error %s" % (result, error)

CALLBACK = FUNTYPE(callback)
</code>
When I call it from Python, I get
<code>TypeError: callback() takes exactly 2 arguments (3 given)
</code>
When I call it from C, I get
<code>warning: passing argument 1 of 'callback' from incompatible pointer type
</code>


A:

I ran into similar problems when I used the <code>ctypes</code> library. I found that the <code>visualstudio_py_util.py</code> module in the <code>visualstudio_py_util</code> extension helped a lot. There's a <code>register_function</code> function in it that automatically transforms the function you need to call into a function that can be called from inside Python.

