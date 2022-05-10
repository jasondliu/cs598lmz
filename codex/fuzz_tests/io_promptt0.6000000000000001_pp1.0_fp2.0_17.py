import io
# Test io.RawIOBase
class TestRawIOBase:
    def test_read(self):
        assert_raises(NotImplementedError, io.RawIOBase().read)

    def test_readinto(self):
        assert_raises(NotImplementedError, io.RawIOBase().readinto, bytearray(1))

    def test_write(self):
        assert_raises(NotImplementedError, io.RawIOBase().write, b'')

    def test_close(self):
        io.RawIOBase().close()

    def test_isatty(self):
        assert not io.RawIOBase().isatty()

    def test_fileno(self):
        assert_raises(UnsupportedOperation, io.RawIOBase().fileno)

    def test_seek(self):
        assert_raises(UnsupportedOperation, io.RawIOBase().seek, 0)

    def test_tell(self):
        assert_raises(UnsupportedOperation, io.RawIOBase().tell)

    def test_truncate(self):
        assert
