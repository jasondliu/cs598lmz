import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

clib = CDLL(os.path.join(os.path.dirname(__file__), "_ctypes_test")).lib
clib.ptr_mode_value.argtypes = [POINTER(S), ctypes.c_int, ctypes.c_int]

def _create_struct():
    s = S()
    s.x = clib.foo_value(3)
    return s

# Holds a pointer
class Ptr(atoma.c_pointer[S]):
    def __init__(self, ptr=None):
        super().__init__(S, ptr)
        # Clear the owned flag: a pointer cannot own
        # anything
        self.owned = False

class TestPassByPointer(unittest.TestCase):
    def test_pass_by_ref(self):
        clib.ptr_mode_ref(Ptr(_create_struct()), 1, 2)

    def test_pass_by_value(self):
        clib.ptr_mode_value(Ptr(_create
