import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42
</code>
I would like to have this code run on both Python 2 and Python 3.
However, for Python 2, <code>ctypes.py_object</code> does not exist, and I have to use <code>ctypes.c_void_p</code> instead.
Is there a way to make this code run on both Python 2 and Python 3?
I tried to do:
<code>if sys.version_info[0] == 2:
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
else:
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
</code>
but it does not work on Python 3.


A:

The problem with your code is that <code>ctypes.py_object</code> is not defined in Python 2.7.
So, to make your code run on both Python 2.7 and 3.x, you can use <code>sys.version_info</code> to check the Python version
