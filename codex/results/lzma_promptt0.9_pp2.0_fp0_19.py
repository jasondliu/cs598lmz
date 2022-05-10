import lzma
# Test LZMADecompressor for doc.
try:
    lzm = lzma.LZMADecompressor()
    lzm.decompress(b"")
except Exception:
    pass

try:
    lzm = lzma.LZMACompressor()
    lzm.compress(b"")
except Exception:
    pass

try:
    lzm = lzma.LZMACompressor(
        format=lzma.FORMAT_AUTO, check=lzma.CHECK_CRC64, preset=0)
    lzm.compress(b"")
except Exception:
    pass


try:
    lzm = lzma.LZMACompressor(
        format=lzma.FORMAT_XZ, check=lzma.CHECK_NONE, preset=9)
    lzm.compress(b"")
    lzm = lzma.LZMADecompressor()
    lzm.decompress(lzm.flush())
except Exception:
    pass



