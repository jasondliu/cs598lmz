import ctypes
# Test ctypes.CFUNCTYPE passing/returning Py_buffer and/or a raw pointer.
# This requires passing all the information to ctypes in this function.
# Used by test_buffer_type()
def BufferCallback(py_buffer, buf_len, some_int, pbuf):
    assert some_int == 4
    assert pbuf.value == 42
    assert pbuf[:buf_len] == b'Hello World'
    return py_buffer.obj

class CallbackTests(unittest.TestCase):

    def setUp(self):
        self.buf = (ctypes.c_ubyte * 15)(*b'Hello WorldHello')

    def test_buffer(self):
        callback = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.c_size_t, ctypes.c_int)(BufferCallback)
        res = ctypes._testfunc(callback, ctypes.py_object('test'), b'Hello World', 4, ctypes.c_void_p(42))
        self.assertEqual(res, 'test
