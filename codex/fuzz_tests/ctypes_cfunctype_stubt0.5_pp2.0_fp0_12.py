import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def callback(f):
    return f()

class TestCallback(unittest.TestCase):
    def test_callback(self):
        self.assertEqual(callback(fun), "hello")

if __name__ == "__main__":
    unittest.main()
