import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'Hello from C'
    return None

cfun = FUNTYPE(fun)

def callback():
    print 'Hello from Python'

cfun.restype = ctypes.py_object
cfun.argtypes = [ctypes.py_object]
cfun(callback)
</code>
However, this is not working. I'm getting the following error:
<code>&gt;&gt;&gt; cfun(callback)
Hello from C
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: argument 1 must be string or read-only character buffer, not instance
</code>
How can I pass a Python callback function to a C function?


A:

You can't do that. The Python callback function is an object which isn't visible to C code.
You could use the <code>ctypes</code> module to call the Python callback, but that's not what you want.
You could also use <code>ctypes</code> to create a C callback function which
