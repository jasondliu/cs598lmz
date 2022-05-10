import ctypes
# Test ctypes.CField
class TestCField:
    def test_comment(self):
        cf = ctypes._CField('char', 'c_char', 1, 'comment')
        assert cf._comment == 'comment'

    def test_initialize(self):
        cf = ctypes._CField('char', 'c_char', 1, 'comment')
        cf.initialize(16)

    def test_getattr(self):
        cf = ctypes._CField('char', 'c_char', 1, 'comment')
        cf.initialize(16)
        cf.getattr(32)


#
