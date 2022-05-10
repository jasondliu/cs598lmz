import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun() # returns b'hello'
</code>
This is expected behavior, as I have specified the return type as <code>ctypes.py_object</code>.
However, I would like to be able to specify the return type as <code>ctypes.c_char_p</code> and have the returned string be <code>b'hello'</code>.
I have tried using <code>ctypes.cast</code> as follows:
<code>ctypes.cast(fun(), ctypes.c_char_p)
</code>
This returns the following error:
<code>AttributeError: 'bytes' object has no attribute 'value'
</code>
I have also tried using <code>ctypes.cast</code> with <code>ctypes.c_char</code> and <code>ctypes.c_char_p</code> as argument types, but this returns <code>b'hello'</code>.
Is there a way to get <code>ctypes.cast</code> to return a <code>b'hello'</code> string when the return
