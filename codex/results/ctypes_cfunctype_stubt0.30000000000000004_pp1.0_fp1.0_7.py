import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This code prints <code>hello</code> as expected.
However, I want to return a function from a function.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return lambda x: x

print fun()(1)
</code>
This code raises <code>TypeError: 'NoneType' object is not callable</code>.
How can I return a function from a function?


A:

The <code>CFUNCTYPE</code> decorator is not designed to be used with a function that returns a function.  It is designed to be used with a function that returns a value.  If you want to return a function, you should use the <code>PYFUNCTYPE</code> decorator instead.
<code>import ctypes
FUNTYPE = ctypes.PYFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return lambda x: x

print fun()(
