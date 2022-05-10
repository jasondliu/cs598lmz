import lzma
# Test LZMADecompressor with multiple input buffers

# The code below is a modified version of the code in the documentation
# for the LZMA module.

comp = lzma.LZMACompressor()
decomp = lzma.LZMADecompressor()

input = b'\x00\x00\x00\x00\x00\x00\x00\x00' + \
        b'This is the original string. ' + \
        b'It is quite long so that it will likely be compressed.'

compressed = comp.compress(input)
compressed += comp.flush()

data = decomp.decompress(compressed)

assert data == input

# Now try the same thing but with multiple calls to decompress().

decomp = lzma.LZMADecompressor()

input = b'\x00\x00\x00\x00\x00\x00\x00\x00' + \
        b'This is the original string. ' + \
        b'It is quite long so that it will likely be compressed.'

