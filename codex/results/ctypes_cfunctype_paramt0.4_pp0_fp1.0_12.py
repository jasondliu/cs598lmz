import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def test_func(a, b):
    return a + b

test_func_c = FUNTYPE(test_func)
print test_func_c(1, 2)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\test.py", line 9, in &lt;module&gt;
    test_func_c = FUNTYPE(test_func)
TypeError: item 1 in _argtypes_ passes a union by value, which is unsupported.
</code>
I am using Python 2.7.3 on Windows 7.
How can I fix this?


A:

This is a known bug in ctypes. See http://bugs.python.org/issue12650

