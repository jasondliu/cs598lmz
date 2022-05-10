import ctypes
# Test ctypes.CFUNCTYPE

def func(a,b):
    return a+b

func_type = ctypes.CFUNCTYPE(ctypes.c_long,ctypes.c_long,ctypes.c_long)
func_type.func_name = 'func'
func_type.errcheck = ctypes.pythonapi.PyErr_CheckSignals

print func_type(1,2)
print func_type(1,2)

print func(1,2)
</code>
I am getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 16, in &lt;module&gt;
    print func_type(1,2)
TypeError: &lt;built-in function func&gt;() takes at most 2 arguments (3 given)
</code>
The error is not coming when I am using <code>ctypes.WINFUNCTYPE</code>. But I want to use <code>CFUNCTYPE</code> as I want to use the same function for both Windows and Linux.
Please help
