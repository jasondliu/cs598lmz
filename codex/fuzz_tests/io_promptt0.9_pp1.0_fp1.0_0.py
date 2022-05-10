import io
# Test io.RawIOBase and io.RawIOBase. An implementation using
# io.RawIOBase must also implement readinto(), and one implementing
# seek() must also implement tell(). Terms of v as a readable buffer:
# - For readinto(): v can be any object supporting the buffer
#   protocol.
# - For read(): len(v) is v.nbytes. v may be any object supporting the
#   read-write buffer protocol, or may be an object which exports
#   the old buffer interface.
# - For write(): len(v) is v.nbytes. v must support the read-write
#   buffer protocol.
import platform
import weakref
PY3 = sys.version_info[0] >= 3

# Helper objects to make test_derrived_io_classes more compact
class BaseRawIO(io.RawIOBase):
    def __init__(self):
        self._mode = None
        self.pos = 0
        self.closed = False

    def readable(self):
        return 'r' in self._mode

    def writable(self):
        return 'w' in self._
