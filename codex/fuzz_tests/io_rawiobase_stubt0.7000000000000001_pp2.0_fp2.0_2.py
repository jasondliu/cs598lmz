import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return self._read_impl(n)

    def write(self, b):
        if not isinstance(b, (bytes, bytearray, memoryview)):
            raise TypeError("write() argument must be a bytes-like object, "
                            "not '%s'" % type(b).__name__)
        return self._write_impl(b)

    def readable(self):
        return self._readable_impl()

    def writable(self):
        return self._writable_impl()

    def seekable(self):
        return self._seekable_impl()


class TextIOBase(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    """Base class for text I/O.

    This class provides a character and line based interface to stream
    I/O. There is no readinto method because Python's character strings
    are immutable. There is no public constructor.

    This class is also the basis for the
