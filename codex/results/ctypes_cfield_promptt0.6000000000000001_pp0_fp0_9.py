import ctypes
# Test ctypes.CField

class TestCF:
    def __init__(self):
        self.value = 1

    def __int__(self):
        return self.value

class TestCField(unittest.TestCase):

    def test_cfield(self):
        class Test(ctypes.Structure):
            _fields_ = [("value", ctypes.CField(TestCF))]

        test = Test()
        self.assertEqual(int(test.value), 1)
        test.value.value = 2
        self.assertEqual(int(test.value), 2)

    def test_cfield_callback(self):
        class Test(ctypes.Structure):
            _fields_ = [("value", ctypes.CField(TestCF))]

        def callback(obj):
            obj.value = 42

        test = Test()
        self.assertEqual(int(test.value), 1)
        ctypes.pythonapi.PyObject_SetAttr(id(test.value),
                                          id(callback.__name__),
                                          id
