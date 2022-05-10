import io
# Test io.RawIOBase for TextIOWrapper's constructor, as happens on
# Python 3.2 on Mac OS X with fast filesystems.

class BrokenRawIO(io.RawIOBase):
    def readable(self):
        return True

    def seekable(self):
        return False

    def readinto(self, b):
        return 0

