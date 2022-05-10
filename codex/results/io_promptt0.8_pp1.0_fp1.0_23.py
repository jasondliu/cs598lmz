import io
# Test io.RawIOBase
class _DelegateIO(io.RawIOBase):
    closed = False
    mode = 'rb'
    name = '<fdopen>'
    softspace = 0
    def close(self):
        self.closed = True
    def fileno(self):
        return 42
# Now test native I/O classes
import fcntl
try:
    import termios
except ImportError:
    pass
class _FileObject(_TestRawIOBase):
    def test_args(self):
        self.assertRaises(TypeError, self.io.FileIO, 'a', 'b', 'c', 'd')
    def test_invalid_mode(self):
        self.assertRaises(ValueError, self.io.FileIO, 'a', 'direct')
    def test_bad_fd(self):
        fd = -5
        self.assertRaises(OSError, self.io.FileIO, fd)
        self.assertRaises(OSError, self.io.FileIO, fd, 'a')
        self.assertRaises(
