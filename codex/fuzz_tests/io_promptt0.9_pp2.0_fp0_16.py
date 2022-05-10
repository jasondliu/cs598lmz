import io
# Test io.RawIOBase.

# This test checks that all read(), write() methods behave identically
# to those implemented by open().  Rather than checking implementation
# details, this test relies on the user operating on buffered data.

# Check read(), read1(), readall()
import _io

# A class inheriting from io.RawIOBase is required.
# Only the abstract methods will be called.
class MyRawIO(_io.RawIOBase):

    def __init__(self):
        self.readall_calls = 0
        self.read1_calls = 0
        self.read_calls = 0

    def readinto(self, b):
        print("MyRawIO .readinto()")
        # Only use read1() internally.
        return self.readall()

    def readall(self):
        print("MyRawIO .readall()")
        self.readall_calls += 1
        return b""

    def read1(self, size=-1):
        print("MyRawIO .read1()")
        self.read1_calls += 1
        return
