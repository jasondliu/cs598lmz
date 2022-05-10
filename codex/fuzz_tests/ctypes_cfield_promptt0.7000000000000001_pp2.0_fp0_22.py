import ctypes
# Test ctypes.CField
#
# We test that 'c_int.in_dll(libc, "i")' works.

class CFieldTest(unittest.TestCase):
    def test(self):
        libc = ctypes.CDLL(ctypes.util.find_library("c"))
        i = ctypes.c_int(42)
        i.value = 17
        self.assertEqual(i.value, 17)
        i.in_dll(libc, "i")
        self.assertEqual(i.value, 42)
        i.value = 17
        self.assertEqual(i.value, 17)

        # this does not work, c_int is not a subclass of ctypes._CData
        #self.assertEqual(i.value, 42)

        # so we need to explicitly trigger the _CData_get() function:
        ctypes._CData_get(i)
        self.assertEqual(i.value, 42)

        # test that we can use CField inside a Structure
        class POINT(ctypes.Structure):
