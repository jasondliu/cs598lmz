import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print(fun())
</code>
<code>python3.6</code> gives the error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(fun())
TypeError: 'str' object is not callable
</code>
<code>python2.7</code> gives the error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(fun())
TypeError: 'str' object is not callable
</code>
I'm using <code>Python 2.7.15</code> and <code>Python 3.6.5</code> on <code>Ubuntu 18.04</code>.
I've tried to look for the answer but I couldn't find anything.
Does anyone know what is going on?


A:

The <code>ctypes</code> module is a C-level binding to the Python C API.  The Python C API is a
