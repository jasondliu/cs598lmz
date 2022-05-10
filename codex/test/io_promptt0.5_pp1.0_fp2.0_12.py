import io
# Test io.RawIOBase
try:
    io.RawIOBase
except AttributeError:
    # Python < 3.2
    class RawIOBase(object):
        pass
    io.RawIOBase = RawIOBase

