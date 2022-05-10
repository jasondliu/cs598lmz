import io
# Test io.RawIOBase instead of io.IOBase to ensure we get read/write/seek
# methods that operate on bytes, not characters.
if hasattr(io, 'RawIOBase'):
    from io import RawIOBase
else:
    from io import BaseRawIO as RawIOBase

