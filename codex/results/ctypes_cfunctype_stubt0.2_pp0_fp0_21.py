import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
This works fine, but I'd like to be able to return a <code>ctypes.c_int</code> instead of a <code>int</code>.
I tried to change the return type of the function to <code>ctypes.c_int</code>, but it doesn't work.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print(fun())
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
I also tried to use <code>ctypes.py_object</code> as the return type, but it doesn't work either.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes
