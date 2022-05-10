import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")
    return "hello world"
</code>
But I get this error:
<code>TypeError: an integer is required (got type str)
</code>
I guess it's because the return value of the function is a string.
Is there a way to make it return a string?


A:

You can use <code>c_char_p</code> as the return type.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    print("hello world")
    return "hello world"
</code>

