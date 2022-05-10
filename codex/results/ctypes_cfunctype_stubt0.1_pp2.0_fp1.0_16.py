import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine, but I would like to be able to return a <code>bytes</code> object instead of a <code>str</code> object.
I tried to change the return type to <code>ctypes.c_char_p</code> but it doesn't work.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return b"hello"

print(fun())
</code>
I get the following error:
<code>TypeError: bytes or integer address expected instead of bytes instance
</code>
I also tried to use <code>ctypes.c_void_p</code> but it doesn't work either.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
@FUNTYPE
def fun():
    return b"hello"

print(fun())
</code>
I get the following error:
<code>TypeError:
