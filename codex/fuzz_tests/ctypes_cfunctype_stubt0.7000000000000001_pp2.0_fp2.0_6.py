import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
</code>
This is a simplified case, in reality the function is a callback for some C library.
How would I call this function from Python?
<code>Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; fun()
TypeError: &lt;built-in function fun&gt; is not a function
</code>


A:

The <code>ctypes</code> module provides a <code>CFUNCTYPE</code> type, which is a Python callable that can be used to call C functions.
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
&gt;&gt;&gt; @FUNTYPE
... def fun():
...     return 42
...
&gt;&gt;&gt; fun
