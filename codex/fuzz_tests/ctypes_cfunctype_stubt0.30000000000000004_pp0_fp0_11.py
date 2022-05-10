import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine, but I would like to be able to return a ctypes string, not a python string.  I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
But I get the error:
<code>TypeError: 'str' does not have the buffer interface
</code>
I also tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return ctypes.c_char_p("hello")

print fun()
</code>
But I get the error:
<code>TypeError: expected LP_c_char, got LP_c_char_p
</code>
How can I return a ctypes string from a function decorated with <code>ctypes.CFUNCTYPE</code>?


A:

