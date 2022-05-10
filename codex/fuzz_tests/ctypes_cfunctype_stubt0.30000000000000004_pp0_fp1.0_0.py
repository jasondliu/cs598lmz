import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine.
But if I try to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code> I get an error:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
<blockquote>
<p>ctypes.ArgumentError: argument 1: : Don't know how to convert parameter 1</p>
</blockquote>
I also tried <code>ctypes.c_char</code> and <code>ctypes.c_char_p</code> but the error is the same.
How can I make this work?


A:

You need to use <code>ctypes.create_string_buffer</code> to create a buffer to return.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@
