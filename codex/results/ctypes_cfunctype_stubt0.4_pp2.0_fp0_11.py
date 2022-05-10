import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine.
But when I try to do the same with a function that takes arguments, it fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    return x

print fun(1)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print fun(1)
TypeError: in method 'fun', argument 1 of type 'PyObject *'
</code>
I've tried using <code>ctypes.c_int</code> instead of <code>ctypes.py_object</code> but that gives a different error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print fun(1)
TypeError: in method 'fun', argument 1 of type
