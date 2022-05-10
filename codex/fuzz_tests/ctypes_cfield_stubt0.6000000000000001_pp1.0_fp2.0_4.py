import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@unittest.skipIf(sys.flags.optimize >= 2,
                 "Docstrings are omitted with -O2 and above")
class Test(unittest.TestCase):
    def test_docstring(self):
        self.assertEqual(ctypes.CField.__doc__, "C compatible field type.")

if __name__ == "__main__":
    unittest.main()
