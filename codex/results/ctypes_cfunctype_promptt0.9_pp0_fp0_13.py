import ctypes
# Test ctypes.CFUNCTYPE(...)(<callback>) ability
class TestCFUNCTYPE(unittest.TestCase):
    def test_basic(self):
        # Check that a callback defined with ctypes.CFUNCTYPE can be
        # passed to C code called with ctypes
        #
        # The callback function used by this test is defined in the C
        # file which is #include-d below.  It is called 'adder'.
        # This function takes a single argument, an instance of
        # ctypes.Structure, and adds 2 to the value of the 'x' field.
        # This tests that ctypes.Structure instances can be passed from
        # Python to C.
        #
        # adder can also be passed NULL, in which case it does nothing.
        #
        # The test repeats this with two different structures, one
        # defined in pure Python, the other in C.
        dll = ctypes.CDLL(_ctypes_test.__file__)

    def test_a_argtypes(self):
        pass
        class X(ctypes.Structure):
           
