import io
# Test io.RawIOBase
class TestRawIOBase(object):
    def test_array_io_base(self):
        self.inner_test_array_io_base()

    def inner_test_array_io_base(self):
        # Make sure RawIOBase is a subclass of IOBase
        assert issubclass(io.RawIOBase, io.IOBase)
        # Make sure all the ABCs are present
        assert issubclass(io.RawIOBase, io.RawIOBase)
        # Make sure the constructor raises a TypeError
        try:
            io.RawIOBase()
        except TypeError:
            pass
        else:
            assert False, "RawIOBase() didn't raise TypeError"
        # Make sure that readinto() is present, and that it raises a TypeError
