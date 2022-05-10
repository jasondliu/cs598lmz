import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "You called a function written in C!"

print fun()
</code>
When I try to run this in my terminal, it returns
<code>Traceback (most recent call last):
  File "./test.py", line 6, in &lt;module&gt;
    print fun()
  File "/usr/lib/python2.7/ctypes/__init__.py", line 366, in __call__
    return self._function(*args)
TypeError: in method 'PyCFuncPtr_call', argument 1 of type 'PyObject *'
</code>
I have tried changing the type of the return value to <code>ctypes.c_void_p</code>, <code>ctypes.c_char_p</code>, and <code>ctypes.c_int</code>. I have also tried using <code>ctypes.c_int.from_address(id(fun))</code> to return the address of the function, but this just returns the address of the <code>fun</code> variable.
What am I doing wrong?


A:

You can
