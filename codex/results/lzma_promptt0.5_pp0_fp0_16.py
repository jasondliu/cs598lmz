import lzma
# Test LZMADecompressor.flush(), which is only available in Python 3.3+
with lzma.LZMADecompressor() as decompressor:
    decompressor.decompress(b'\x00')
    decompressor.flush()

with lzma.LZMAFile(io.BytesIO(b'\x00')) as f:
    assert f.read() == b''
