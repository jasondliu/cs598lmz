import io
# Test io.RawIOBase and io.BufferedIOBase

import io

class MockRawIO(io.RawIOBase):
    def readinto(self, b):
        return 0

class MockBufferedIO(io.BufferedIOBase):
    def readinto(self, b):
        return 0

class MockNonBlockWriterIO(io.RawIOBase):
    def write(self, b):
        return 0

class MockNonBlockReaderIO(io.RawIOBase):
    def readinto(self, b):
        return 0

class MockBlockWriterIO(io.RawIOBase):
    def write(self, b):
        return 0

    def writable(self):
        return True

class MockBlockReaderIO(io.RawIOBase):
    def readinto(self, b):
        return 0

    def readable(self):
        return True

# Issue #26254: check that the io module does not import the _io module
# at the C level.
