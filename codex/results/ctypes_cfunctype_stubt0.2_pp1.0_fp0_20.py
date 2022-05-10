import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works fine. But if I try to return <code>None</code> instead of <code>"hello"</code>, I get a <code>TypeError</code>:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

print(fun())
</code>
<blockquote>
<p>TypeError: NoneType is not a subtype of py_object</p>
</blockquote>
Why is this? Is there a way to return <code>None</code>?


A:

<code>ctypes.py_object</code> is a <code>ctypes</code> type that represents a Python object.  It's not a Python object itself.  It's a C type.  It's a pointer to a Python object.  So you can't return <code>None</code> from a function that returns a <code>ctypes.py_object</code>, because <code>None</code> is not
