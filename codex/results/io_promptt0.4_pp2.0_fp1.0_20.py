import io
# Test io.RawIOBase

class MockRawIO(io.RawIOBase):
    def __init__(self, read_stack, write_stack):
        self.read_stack = read_stack
        self.write_stack = write_stack

    def readinto(self, b):
        data = self.read_stack.pop(0)
        n = len(b)
        b[:len(data)] = data
        return n

    def write(self, b):
        self.write_stack.append(bytes(b))
        return len(b)

class MockNonBlockWriterIO(MockRawIO):
    def write(self, b):
        raise BlockingIOError

class MockNonBlockReaderIO(MockRawIO):
    def readinto(self, b):
        raise BlockingIOError

class MockNonBlockIO(MockRawIO):
    def readinto(self, b):
        raise BlockingIOError
    def write(self, b):
        raise BlockingIOError

class TestRawIO(unittest.TestCase):
    def test_
