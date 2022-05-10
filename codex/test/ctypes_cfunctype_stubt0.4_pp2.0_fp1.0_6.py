import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_c_function(self):
    # ctypes.CFUNCTYPE(ctypes.py_object)
    f = fun
    self.assertEqual(f(), None)

