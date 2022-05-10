import lzma
# Test LZMADecompressor

# Test for issue #14894: LZMADecompressor.decompress() should accept
# bytes-like objects.

# Test for issue #14894: LZMADecompressor.decompress() should accept
# bytes-like objects.

import io
import lzma

def test_decompress_bytes():
    data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
    c = lzma.LZMADecompressor()
    assert c.decompress(data) == b'hello'
    assert c.unused_data == b''
    c = lzma.LZMADecompressor()
    assert c.decompress(memoryview(data)) == b'hello'
    assert c.unused_data == b''
    c = lzma.LZMAD
