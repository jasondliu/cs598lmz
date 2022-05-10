import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object()

fun()
</code>
This gives the error, indicating py_objects are not supported for return types for function pointers.
<code>Traceback (most recent call last):
  File "testpyobj.py", line 5, in &lt;module&gt;
    @FUNTYPE
  File "/usr/lib64/python3.4/ctypes/__init__.py", line 329, in __getitem__
    func = self._make_function_type(args)
  File "/usr/lib64/python3.4/ctypes/__init__.py", line 1059, in _make_function_type
    raise TypeError("don't know how to handle %s" % restype)
TypeError: don't know how to handle py_object
</code>
I have tried to subclass ctypes.py_object() and override the _type_ to use the c_void_p _type_ but this doesn't seem to do the trick. 
To clarify the end goal: 
I want to be able to pass wrapped c-functions with py
