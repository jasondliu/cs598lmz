import io
# Test io.RawIOBase.seekable() method

import _io

class MockRawIO(_io.RawIOBase):
    def __init__(self, seekable):
        self.seekable = seekable

def test_seekable_1():
    # Test with a seekable file.
    f = MockRawIO(seekable=True)
    assert f.seekable() is True

def test_seekable_2():
    # Test with a non-seekable file.
    f = MockRawIO(seekable=False)
    assert f.seekable() is False

def test_seekable_3():
    # Test with a file that can seek both forward and backwards.
    f = MockRawIO(seekable=True)
    f.seek(0)
    f.tell()
    f.seek(-1, 1)
    f.tell()
    assert f.seekable() is True

def test_seekable_4():
    # Test with a file that can only seek backward.
    f = MockRawIO(seekable=True)
    f.seek(0)

