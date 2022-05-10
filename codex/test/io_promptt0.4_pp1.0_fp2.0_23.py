import io
# Test io.RawIOBase
class TestRawIOBase(object):
    def test_read(self):
        # Test RawIOBase.read()
        class MyRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:3] = b'foo'
                return 3
            def readall(self):
                return b'foobar'
        r = MyRawIO()
        assert r.read(5) == b'fooba'
        assert r.read() == b'r'
        assert r.read() == b''
        assert r.readall() == b'foobar'
        assert r.readall() == b''
        r = MyRawIO()
        assert r.read(5) == b'fooba'
        assert r.read() == b'r'
        assert r.read() == b''
        assert r.readall() == b'foobar'
        assert r.readall() == b''
        r = MyRawIO()
