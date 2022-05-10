import io
# Test io.RawIOBase and io.BufferedIOBase inherit from IOBase
issubclass(io.RawIOBase, io.IOBase)
issubclass(io.BufferedIOBase, io.IOBase)
# Verify Flushable and Seekable are included
