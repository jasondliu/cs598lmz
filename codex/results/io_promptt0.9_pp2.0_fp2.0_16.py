import io
# Test io.RawIOBase subclass


def test_RawIOBase_subclass_write():
    class TestRawIO(io.RawIOBase):

        def write(self, b):
            self.b = b
    testio = TestRawIO()

    assert testio.write(b'testing') == 7
    assert testio.b == b'testing'


def test_RawIOBase_subclass_read():
    class TestRawIO(io.RawIOBase):

        def read(self, b):
            self.b = b
    testio = TestRawIO()

    assert testio.read(-1) == b''
    assert testio.b == -1

# Test BufferedIOBase subclass


def test_BufferedIOBase_subclass_readable():
    class TestBufferedIO(io.BufferedIOBase):

        def readable(self):
            return False
    testio = TestBufferedIO()

    assert testio.readable() == False


def test_BufferedIOBase_subclass_readinto():
    class TestBufferedIO(io.BufferedIOBase):
