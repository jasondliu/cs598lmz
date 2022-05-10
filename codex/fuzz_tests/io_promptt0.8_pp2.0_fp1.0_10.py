import io
# Test io.RawIOBase as a base class
import _pyio as pyio
assert issubclass(pyio.RawIOBase, io.RawIOBase)
assert issubclass(pyio.BufferedIOBase, io.BufferedIOBase)
assert issubclass(pyio.TextIOBase, io.TextIOBase)
# Test the io module itself
import io as _io
assert _io.DEFAULT_BUFFER_SIZE == 8*1024
assert _io.BlockingIOError.errno == pyio.BlockingIOError.errno
assert _io.BlockingIOError.strerror == pyio.BlockingIOError.strerror
assert _io.UnsupportedOperation.errno == pyio.UnsupportedOperation.errno
assert _io.UnsupportedOperation.strerror == pyio.UnsupportedOperation.strerror
assert _io.SEEK_SET == pyio.SEEK_SET
assert _io.SEEK_CUR == pyio.SEEK_CUR
assert _io.SEEK_END == pyio.SEEK_END
assert _io.open == pyio.
