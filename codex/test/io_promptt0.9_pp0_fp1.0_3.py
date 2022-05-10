import io
# Test io.RawIOBase separately from io.BytesIO (which inherits from it).
# This is done because implementations are not required to support the
# RawIOBase methods in a consistent way, and e.g. Python may implement BytesIO
# (which is a file-like object) using an in-memory buffer, but RawIOBase
# using a real file handle.

if hasattr(io, 'RawIOBase'):

    class MyRawIO(io.RawIOBase):

        def readinto(self, b):
            return 0

    class MyRawIOSub(MyRawIO):

        def __init__(self):
            self.closed = 0

        def readable(self):
            return True

        def seekable(self):
            return False

