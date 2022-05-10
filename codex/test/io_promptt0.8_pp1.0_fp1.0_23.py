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
