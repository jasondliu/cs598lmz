import ctypes
# Test ctypes.CField
class TestCField:
    @pytest.mark.xfail(reason='ctypes.CField is not a subclass of ctypes.Field')
    def test_CField_is_Field(self):
        assert issubclass(ctypes.CField, ctypes.Field)
        assert issubclass(ctypes.CField, ctypes.CData)

    def test_CField_init(self):
        f = ctypes.CField('name', ctypes.c_int, 42, offsetof=0)
        assert f.name == 'name'
        assert f.type is ctypes.c_int
        assert f.offset == 0
        assert f.size == ctypes.sizeof(ctypes.c_int)
        assert f.bitsize == 8 * ctypes.sizeof(ctypes.c_int)
        assert f.bitshift == -1

    @pytest.mark.xfail(reason='ctypes.CField doesn\'t have a flag attribute')
    @pytest.mark.skipif(IS_CPYTHON and sys.version_info
