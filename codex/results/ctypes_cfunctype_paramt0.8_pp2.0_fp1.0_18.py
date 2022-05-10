import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)


class TestCallback(unittest.TestCase):

    def test_callback_1(self):
        context = Context(API_VERSION)
        callback = FUNTYPE(callback_1_int)
        context.set_error_callback(callback)
        self.assertEqual(context.error_callback, callback)

    def test_callback_2(self):
        context = Context(API_VERSION)
        callback = FUNTYPE(callback_2_int)
        context.set_error_callback(callback_2)
        self.assertEqual(context.error_callback, callback)

    def test_callback_3(self):
        context = Context(API_VERSION)
        callback = FUNTYPE(callback_3_int)
        context.set_error_callback(callback)
        self.assertEqual(context.error_callback, callback)

    def test_callback_object(self):
        context = Context(API_VERSION)
        callback = CallbackObject()
        context.set_error_callback(callback)
        self.assertE
