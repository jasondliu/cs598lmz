import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    y = 'XX'
    return y

def test_fun():
    x = fun()
    assert x == 'XX'
</code>
This works, but I am not sure that it's the right way to do it in Python.

