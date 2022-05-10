import io
# Test io.RawIOBase

import _io

# Issue #17981: io.RawIOBase.readinto() should accept a memoryview.
class MemoryViewLike:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]

# Issue #17982: io.RawIOBase.readinto() should accept an array.
class ArrayLike:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]
    def tobytes(self):
        return self.data

# Issue #17983: io.RawIOBase.readinto() should accept a bytearray.
class BytearrayLike:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return
