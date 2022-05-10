import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class Test_ctypes_CFUNCTYPE(BaseTestCheck):
    def test_ctypes_CFUNCTYPE(self):
        self.run_test(fun)
