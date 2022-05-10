import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(a):
    return a + 1

c_func = FUNTYPE(py_func)

print(c_func(1))
</code>
This is the error message:
<code>Traceback (most recent call last):
  File "C:/Users/user/Desktop/test.py", line 9, in &lt;module&gt;
    c_func = FUNTYPE(py_func)
TypeError: must be real number, not function
</code>
I am using Python 3.6.7.


A:

I found the answer. We need to use <code>ctypes.pythonapi.PyCFunction_New</code> to convert the python function to a c function.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(a):
    return a + 1

c_func = FUNTYPE(ctypes.pythonapi.PyCFunction_New(py
