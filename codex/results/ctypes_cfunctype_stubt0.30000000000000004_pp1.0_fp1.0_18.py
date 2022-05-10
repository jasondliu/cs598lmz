import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print fun()
</code>
This works fine. But when I try to return a dict instead of a string, it throws an error.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return {"a":1}

print fun()
</code>
Error:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print fun()
  File "/usr/lib/python2.7/dist-packages/ctypes/__init__.py", line 366, in __call__
    return self._function(*args)
TypeError: in method 'fun', argument 1 of type 'PyObject *'
</code>
I tried using <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code>, but it doesn't work.
I also tried using <code>ctypes.c_char_p</code> and then <code
