import lzma
# Test LZMADecompressor arguments
# Invalid argument type
with lzma.LZMADecompressor() as d:
    d.decompress(b"", invalid_arg=1)
# Invalid argument value
with lzma.LZMADecompressor() as d:
    d.decompress(b"", format=1)
# Invalid argument name
with lzma.LZMADecompressor() as d:
    d.decompress(b"", invalid_key=1)
# Invalid argument name, but valid keyword
with lzma.LZMADecompressor() as d:
    d.decompress(b"", format="no value")
# Invalid argument name
with lzma.LZMADecompressor() as d:
    d.decompress(b"", invalid_key="no value")
# Test LZMADecompressor.copy() arguments
# Invalid argument type
with lzma.LZMADecompressor() as d:
    d.copy(invalid_arg=1)
# Invalid argument value
with lz
