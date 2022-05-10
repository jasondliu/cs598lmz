import io
# Test io.RawIOBase used as return value.

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        return

class MyBytesRawIO(io.RawIOBase):
    def readinto(self, b):
        return len(b)

class MyIterBytesRawIO(io.RawIOBase):
    def readinto(self, b):
        return len(b)

    def __iter__(self):
        return iter(b"")

class TestWithStatement:
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass

# Issue #16347
class TestClass(MyRawIO):
    def __enter__(self):
        return 42
    def __exit__(self, *args):
        pass

def raw_test():
    with TestClass() as f:
        print('done')

def raw_test_bytes():
    with TestClass() as f:
        print('done')

