import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ioctl_parser.RET_T, ioctl_parser.ARGS_T)

class IOCTLRequest(ctypes.Structure):
    _fields_ = [
            ('code', ctypes.c_int),
            ('arg', ctypes.c_void_p)
    ]

class TestIOCtl(unittest.TestCase):

    def test_ioctl_parser(self):
        def test_func(value):
            test_value = value
            def test_func2(obj, func, arg):
                nonlocal test_value
                self.assertEqual(obj, 'test')
                self.assertEqual(func, 1)
                self.assertEqual(arg, test_value)
                return 'test'
            return test_func2
        parser = ioctl_parser.IOCtlParser('test', test_func)
        for i in range(0, 0x40000000):
            parser(i)

    def test_ioctl_parser2(self):
        def test_func():
            def test_func2(obj,
