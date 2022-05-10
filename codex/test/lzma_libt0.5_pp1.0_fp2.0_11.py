import lzma
lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)

# Check that we can handle a file with a bad header.
lzma.LZMADecompressor(format=lzma.FORMAT_ALONE).decompress(b'\x00')

# Check that we can handle a file with a bad stream.
