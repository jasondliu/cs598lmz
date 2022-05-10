import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
This works, but I don't know how to pass arguments to the function. I tried this:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(arg):
    return arg

fun("hello")
</code>
But this gives me the following error:
<code>TypeError: expected a character buffer object
</code>
I also tried to pass <code>ctypes.c_char_p</code> as the argument type, but that didn't work either.
How can I pass arguments to this function?


A:

I found the answer to my question here:
https://stackoverflow.com/a/8136518/109942
The problem is that the <code>ctypes.py_object</code> type is not a valid type for the <code>ctypes.CFUNCTYPE</code> constructor.

