import io
# Test io.RawIOBase

class MockRawIO(io.RawIOBase):
    def readinto(self, buf):
        return 0

def test_rawiobase():
    io_obj = MockRawIO()

# Try to exercise every base IOBase method
def exercise_base_methods(self):
    self.fileno()
    self.seekable()
    self.readable()
    self.writable()
    #self.isatty()
    self.read()
    self.readable() and self.readline()
    self.readable() and self.readlines()
    self.writable() and self.write("t")
    self.writable() and self.writelines(["test"])
    self.readable() and self.seek(0,1)
    self.readable() and self.tell()
    self.close()

def test_io_methods(raw, buf):
    exercise_base_methods(raw)
    exercise_base_methods(buf)

    # Test __enter__/__exit__
    with raw:
        exercise_
