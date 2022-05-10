import io
# Test io.RawIOBase
class RawIOBase(io.RawIOBase):
    def read(self, n=-1):
        return b'abc'
    def write(self, b):
        return len(b)

class RawIO(RawIOBase):
    def fileno(self):
        return 42

class AppTestRawIOBase:
    def setup_class(cls):
        cls.w_testfile = cls.space.wrap(str(udir.join('io-raw-base.txt')))

    def test_constructor(self):
        # Test RawIOBase constructor
        raises(TypeError, io.RawIOBase)

    def test_attributes(self):
        # Test RawIOBase attributes
        r = RawIO()
        assert r.mode == 'rb'
        assert r.name == None
        assert r.closed == False

    def test_read(self):
        # Test RawIOBase read()
        r = RawIO()
        assert r.read() == b'abc'
        assert r.read(4) == b'abc'
       
