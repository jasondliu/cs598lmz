import bz2
# Test BZ2Decompressor with a file-like object

try:
    import io
except ImportError:
    io = None

bz2_data = bz2.compress(b"Some data")

# a file-like object
class TestIO(io.BytesIO):
    def read(self, n=None):
        raise OSError()

def test_file_like():
    # Test that a file-like object is checked for a readable() method
    d = bz2.BZ2Decompressor()

    # Read from a file-like object with a read() method
    io_obj = io.BytesIO(bz2_data)
    decompressed = d.decompress(io_obj)
    assert decompressed == b"Some data"

    # Read from a file-like object without a read() method
    io_obj = TestIO(bz2_data)
    decompressed = d.decompress(io_obj)
    assert decompressed == b"Some data"

