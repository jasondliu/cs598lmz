import lzma
# Test LZMADecompressor's ability to decompress a multi-stream file
# with a non-zero Uncompressed Size in the end of stream marker.

bytestring = b"".join([
    b"\x00\x00\x00\x00\x00\x00\x00\x10",  # Uncompressed Size in the end of stream marker.
    lzma.compress(b"foo"),
    lzma.compress(b"bar"),
    lzma.compress(b"baz"),
    lzma.compress(b""),
])

decompressor = lzma.LZMADecompressor()

data = decompressor.decompress(bytestring)
print(data)
