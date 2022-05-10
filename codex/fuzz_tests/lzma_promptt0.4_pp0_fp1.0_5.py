import lzma
# Test LZMADecompressor.flush() with a non-seekable file.
# This should raise an exception.
with open('lzma_compressed_file.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with pytest.raises(IOError):
        decompressor.flush(f)
# Test LZMADecompressor.flush() with a seekable file.
with open('lzma_compressed_file.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    decompressor.flush(io.BytesIO(f.read()))
# Test LZMADecompressor.flush() with a seekable file and
# LZMADecompressor.unused_data.
with open('lzma_compressed_file.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    decompressor.decompress(f.read())
    decompressor.flush(io.BytesIO(decompressor.
