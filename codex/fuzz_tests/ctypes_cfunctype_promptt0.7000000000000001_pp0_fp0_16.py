import ctypes
# Test ctypes.CFUNCTYPE with callback in class method and instance attribute.

if os.name == 'nt':
    import _ctypes_test
elif sys.platform == 'darwin':
    import ctypes.macholib._ctypes_test as _ctypes_test
else:
    import _ctypes_test

class X(object):
    def __init__(self):
        self.callback = None

    def test(self, arg):
        return self.callback(arg)

    def test_int(self, arg):
        i = self.callback(arg)
        return i

class Y(X):
    def __init__(self):
        X.__init__(self)

if os.name == 'nt':
    CallbackType = ctypes.WINFUNCTYPE
else:
    CallbackType = ctypes.CFUNCTYPE

CallbackInstance = CallbackType(ctypes.c_int, ctypes.c_int)

class Test(unittest.TestCase):
    def test(self):
        x = X()
        callback =
