import lzma
# Test LZMADecompressor
with lzma.LZMADecompressor() as d:
    x = d.decompress(b"\x00\x00\x00\x00\xa3\x01\x00\x00\x00\x00\x00\x00" +
          b"ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert x == b"ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
import lzma
# Test LZMADecompressor with non-seekable file-like object
class TestFile(io.TextIOWrapper):
    def seekable(self):
        return False

input_file = TestFile(io.BytesIO(b"\x00\x00\x00\x00\xa3\x01\x00\x00\x00\x00\x00\x00" +
        b"ABCDEFGHIJKLMNOPQ
