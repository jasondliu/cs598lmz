import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world!"

print fun()
</code>
This code prints <code>Hello, world!</code> as expected.
However, if I change the return type to <code>ctypes.c_char_p</code>, I get a segmentation fault.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "Hello, world!"

print fun()
</code>
What's going on here?


A:

You're returning an object that is not a <code>c_char_p</code> (a pointer to a C string).  You need to convert the string to a <code>c_char_p</code> using the <code>ctypes.c_char_p</code> constructor:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return ctypes.c_char_p("Hello, world!")

print fun
