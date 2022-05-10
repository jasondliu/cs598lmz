import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine, but I want to be able to return a <code>ctypes.c_char_p</code> instead of a <code>str</code>.
I tried to do this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
But I get this error:
<code>TypeError: expected bytes, str found
</code>
I also tried to do this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return ctypes.c_char_p("hello")

print(fun())
</code>
But I get this error:
<code>TypeError: expected bytes, c_char_p found
</code>
How can I return a <code>ctypes.c_char_p</code> from a <
