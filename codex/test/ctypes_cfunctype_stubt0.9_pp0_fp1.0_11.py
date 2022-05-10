import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return

def f():
    try:
        fun()
    except Exception as e:
        assert type(e) is TypeError
        print(e)
    else:
        assert 0

