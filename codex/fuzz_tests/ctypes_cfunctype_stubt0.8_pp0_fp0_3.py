import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class test(unittest.TestCase):
    def test_1(self):
        "Check that None is correctly returned"
        self.assertEqual(None, fun())

    def test_2(self):
        "Check that None has the correct type"
        self.assertEqual(type(None), type(fun()))

if __name__ == "__main__":
    unittest.main()
