import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test_create_unicode_buffer(BaseTestCheck):
    def test_create_unicode_buffer(self):
        buffer = ctypes.create_unicode_buffer(10)
        assert isinstance(buffer, ctypes.Array)
        assert isinstance(buffer, ctypes.c_wchar)
        assert len(buffer) == 10
        assert buffer[0] == u"\x00"
        raises(IndexError, "buffer[10]")
        raises(TypeError, ctypes.create_unicode_buffer, 'abc')
        raises(TypeError, ctypes.create_unicode_buffer, buffer)

    def test_setitem(self):
        buffer = ctypes.create_unicode_buffer(10)
        buffer[5] = 'x'
        assert buffer[5] == u'x'
        raises(ValueError, "buffer[5] = 5")
        raises(TypeError, "buffer[5] = 'a'*2")

class Test_create_string_buffer(BaseTestCheck):
    def test_create_string
