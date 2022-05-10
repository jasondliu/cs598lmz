import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CMember = object

@support.cpython_only
class CDLLTestCase(unittest.TestCase):
    """Tests CDLL functions.
    """

    def setUp(self):
        self.cdll = ctypes.CDLL(ctypes.util.find_library('c'))

    def test_dll_handle(self):
        self.cdll._handle
        dlopen = ctypes.CDLL(ctypes.util.find_library('dl'))
        dlopen.dlopen.restype = ctypes.c_void_p
        dlopen.dlopen(None, 0)
        handle = dlopen.dlopen(self.cdll._name, dlopen.RTLD_GLOBAL | dlopen.RTLD_NOW)
        self.assertEqual(handle, self.cdll._handle)

    def test_func_type(self):
        # ctypes.CFUNCTYPE(restype, *argtypes)
        #
        # Create a ctypes function prototype.  restype is the
