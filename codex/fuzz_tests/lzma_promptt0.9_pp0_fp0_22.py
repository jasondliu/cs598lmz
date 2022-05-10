import lzma
# Test LZMADecompressor with an input less than 23 bytes.  A LZMADecompressor
# with an input less than 23 bytes must return nothing.
from lzma import LZMADecompressor
d = LZMADecompressor()
assert d.decompress(b'abc') == b''
# Test is_check_supported on various stream types.
for check_type in (0, lzma.CHECK_NONE, lzma.CHECK_CRC32, lzma.CHECK_CRC64,
                   lzma.CHECK_SHA256):
    assert lzma.is_check_supported(check_type)
# Test that is_check_supported() raises ValueError for unknown check_type.
with pytest.raises(ValueError):
    lzma.is_check_supported(999)
# Test that is_check_supported() raises a TypeError for nonintegers.
with pytest.raises(TypeError):
    lzma.is_check_supported('lzma')
# Test that 0x1000000U is handled as a valid FLAGS value
