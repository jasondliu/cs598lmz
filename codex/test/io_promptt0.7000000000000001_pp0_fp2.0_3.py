import io
# Test io.RawIOBase
from io import RawIOBase
# Test io.BufferedIOBase
from io import BufferedIOBase
# Test io.TextIOBase
from io import TextIOBase


# Test exception processing.

def test_exception_args():
    """Test that sys.exc_info() returns argument tuple."""
