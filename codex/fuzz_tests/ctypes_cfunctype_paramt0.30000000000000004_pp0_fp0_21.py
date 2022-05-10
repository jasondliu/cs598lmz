import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def _callback(arg):
    print("_callback", arg)
    return 0

_callback_func = FUNTYPE(_callback)

def callback(arg):
    print("callback", arg)
    return 0

class Test(unittest.TestCase):
    def test_callback(self):
        self.assertEqual(_callback_func(0), 0)
        self.assertEqual(_callback_func(1), 0)
        self.assertEqual(_callback_func(2), 0)

    def test_callback_func(self):
        self.assertEqual(callback(0), 0)
        self.assertEqual(callback(1), 0)
        self.assertEqual(callback(2), 0)

if __name__ == '__main__':
    unittest.main()
