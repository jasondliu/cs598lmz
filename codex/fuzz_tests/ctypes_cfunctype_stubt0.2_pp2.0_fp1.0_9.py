import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine, but I would like to be able to pass arguments to the function. I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg

print fun("hello")
</code>
But this gives me a <code>TypeError: argument 1 must be string without null bytes, not str</code>. I tried to convert the string to a <code>ctypes.c_char_p</code> but that didn't work either.
How can I pass a string to a function that is decorated with <code>ctypes.CFUNCTYPE</code>?


A:

You need to use <code>ctypes.c_char_p</code> for the argument type.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_char_p)
@FUNTYPE
def fun(arg):
