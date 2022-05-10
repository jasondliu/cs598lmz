import io
# Test io.RawIOBase
# io.TextIOBase
"""
class io.RawIOBase:
    def read(self, size=-1):
        [...]
    def readall(self):
        [...]
    def readinto(self, b):
        [...]
    def write(self, b):
        [...]
"""
class TestRawIOBase(io.RawIOBase):
    def read(self, size=-1):
        return "test"
    def readall(self):
        return "test"
    def readinto(self, b):
        return "test"
    def write(self, b):
        return "test"
# Test io.TextIOBase
# io.BufferedIOBase
"""
class io.BufferedIOBase(RawIOBase):
    def read(self, size=-1):
        [...]
    def read1(self, size=-1):
        [...]
    def readinto(self, b):
        [...]
    def write(self, b):
        [...]
    def detach(self):
        [...]
"""
