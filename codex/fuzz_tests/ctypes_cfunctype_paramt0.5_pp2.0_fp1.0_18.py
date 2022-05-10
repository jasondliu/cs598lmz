import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def double_it(x):
    return 2*x

def py_func_to_c_func(func):
    c_func = FUNTYPE(func)
    return c_func

if __name__ == "__main__":
    c_func = py_func_to_c_func(double_it)
    print(double_it(3))
    print(c_func(3))
</code>
The error I get is:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    c_func = py_func_to_c_func(double_it)
  File "test.py", line 9, in py_func_to_c_func
    c_func = FUNTYPE(func)
TypeError: argument 1 must be a native function
</code>
Any idea what's going on?


A:

You need to use the <code>ctypes.CFUNCTYPE</code
