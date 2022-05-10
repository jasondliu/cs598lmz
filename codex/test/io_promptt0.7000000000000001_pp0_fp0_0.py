import io
# Test io.RawIOBase
try:
    from io import UnsupportedOperation
except ImportError:
    from io import BlockingIOError as UnsupportedOperation

