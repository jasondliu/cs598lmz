import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello, fun!"
def fun2():
    return "hello, fun2!"

class Test(unittest.TestCase):

    def test_cffi_call_pyfunc(self):
        res = ffi.pyapi.PyRun_String("ffi.new('PyObject *', fun)()")
        assert ffi.string(res) == 'hello, fun!'

    if sys.version_info >= (3,):
        def test_cffi_call_pyfunc_bytes(self):
            res = ffi.pyapi.PyRun_String("ffi.new('PyObject *', fun2)()")
            assert ffi.string(res) == b'hello, fun2!'
    
    def test_cffi_call_capsule(self):
        # caps = ffi.new('void *', ffi.addressof(ffi.new('char[]', 'hello')))
        # res = ffi.pyapi.PyCapsule_CheckExact(caps)
        res = ffi.pyapi.PyC
