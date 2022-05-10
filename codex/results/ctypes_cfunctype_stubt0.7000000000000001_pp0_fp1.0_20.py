import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hey")
    return "hello"
</code>
Now I can pass <code>fun</code> to a C function to call it. But when I call <code>fun()</code> from Python, I get <code>None</code> instead of <code>"hello"</code>.
How can I get the expected behavior?


A:

The answer to the question is the same as this one:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(obj):
    print("hey")
    return "hello"
</code>

