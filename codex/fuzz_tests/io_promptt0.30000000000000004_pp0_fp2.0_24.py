import io
# Test io.RawIOBase

class TestRawIOBase:

    def test_read(self):
        # test that read() returns an empty bytes object at EOF
        rawio = io.RawIOBase()
        assert rawio.read(1) == b''

    def test_readinto(self):
        # test that readinto() returns 0 at EOF
        rawio = io.RawIOBase()
        b = bytearray(1)
        assert rawio.readinto(b) == 0

    def test_readall(self):
        # test that readall() returns an empty bytes object at EOF
        rawio = io.RawIOBase()
        assert rawio.readall() == b''

    def test_read1(self):
        # test that read1() returns an empty bytes object at EOF
        rawio = io.RawIOBase()
        assert rawio.read1(1) == b''

    def test_readable(self):
        # test that RawIOBase is readable
        assert io.RawIOBase().readable()

    def test_seek(self):
       
