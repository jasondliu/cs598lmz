import io
# Test io.RawIOBase
def test_RawIOBase():
    _io.RawIOBase()
    try:
        class MyRawIO(_io.RawIOBase):
            def fileno(self): pass
            def readinto(self, a): pass
    except TypeError:
        pass
    try:
        class MyRawIO(_io.RawIOBase):
            def __init__(self): pass
            def readinto(self, a): pass
    except TypeError:
        pass
    try:
        class MyRawIO(_io.RawIOBase):
            def __init__(self): pass
            def fileno(self): pass
    except TypeError:
        pass
    try:
        class MyRawIO(_io.RawIOBase):
            pass
    except TypeError:
        pass
# Test io.BufferedIOBase
def test_BufferedIOBase():
    _io.BufferedIOBase()
    try:
        class MyBufferedIO(_io.BufferedIOBase):
            def readable(self): pass
            def readinto(self, a): pass
            def read1
