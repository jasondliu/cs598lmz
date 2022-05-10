import io
# Test io.RawIOBase instead of io.IOBase, since Python 2.6 does not
# implement io.IOBase.
class FakeRawIO(io.RawIOBase):
    def read(self, size=None):
        return b'x' * (size or 1)
    def seekable(self):
        return True
    def write(self, b):
        pass

def test_fakeio():
    # Issue #22348: when writing to a file with a raw I/O interface,
    # make sure that a short write raises BlockingIOError instead of
    # returning None.
    class MyRawIO(io.RawIOBase):
        def writable(self):
            return True
        def write(self, b):
            return 0
    i = MyRawIO()
    with pytest.raises(BlockingIOError) as excinfo:
        i.write(b"data")
    assert excinfo.value.characters_written == 0
    assert excinfo.value.characters_wanted == 4
    assert excinfo.value.errno == errno.EAGAIN


