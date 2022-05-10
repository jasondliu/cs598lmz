import lzma
# Test LZMADecompressor
#
# This test is intended to test the LZMADecompressor class.
#
# The test is based on the example in the documentation of the LZMA module.

from io import BytesIO
from lzma import LZMADecompressor, LZMAError

def test_decompressor():
    # Test the decompressor with a small example.
    data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
    f = BytesIO(data)
    decompressor = LZMADecompressor()
    assert decompressor.decompress(f.read(1)) == b''
    assert decompressor.decompress(f.read()) == b'hello'
    assert decompressor.unused_data == b''
    assert decompressor.eof is True

    # Test the decompressor with a small example.
    data
