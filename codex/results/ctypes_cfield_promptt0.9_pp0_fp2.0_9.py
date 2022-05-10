import ctypes
# Test ctypes.CFields


class TestCFields(object):
    def test_byref(self):
        tp = ctypes.CFields(None, None, None, 0)
        assert tp.byref()._type_ == tp

    def test_in_dll(self):
        import _ctypes_test
        field = ctypes.CFields(_ctypes_test.lib, "TestCFieldsStruct",
                               "a", ctypes.c_int)
        assert hasattr(field, "_in_dll")

    def test_in_dll_lacks(self):
        field = ctypes.CFields(None, None, "a", ctypes.c_int)
        assert not hasattr(field, "_in_dll")

    def test_offset(self):
        sz = ctypes.sizeof(ctypes.c_char)
        field = ctypes.CFields(None, None, "a", ctypes.c_char, offset=3*sz)
        assert field.offset == 3

    def test_offset_instance(self
