import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
This works, but I don't know how to return a string.
I tried to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code>, but it doesn't work.
I also tried to use <code>ctypes.c_char_p</code> as the return type and <code>ctypes.c_char_p(b"hello")</code> as the return value, but it doesn't work either.
How can I return a string?


A:

You can use <code>ctypes.c_char_p</code> as the return type, but you have to pass a <code>bytes</code> object to the function.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return b"hello"

print(fun())
</code>

