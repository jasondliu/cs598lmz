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
