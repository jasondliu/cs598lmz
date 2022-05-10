import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

s = fun()
print s
</code>
I would like to understand why the last line of code gives me an error:
<code>print s
TypeError: 'str' object is not callable
</code>
I am expecting the output to be <code>hello</code>.

