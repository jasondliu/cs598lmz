import lzma
# Test LZMADecompressor
dec = lzma.LZMADecompressor()
_ = dec.decompress(b'x\x9c1\x10\x00\x00')

# Test LZMACompressor
comp = lzma.LZMACompressor()
_ = comp.compress(b'foo')
_ = comp.flush()
# Test LZMACompressor with filter chain
comp = lzma.LZMACompressor(filters=[
    {"id": lzma.FILTER_LZMA2, "preset": 3 | lzma.PRESET_EXTREME}
])
_ = comp.compress(b'foo')
_ = comp.flush()

# Test error messages from C extension
try:
    lzma.decompress(b'x\x9c1\x10\x00\x00')
except Exception as e:
    e.args[0]
    # Non-innocuous decompression options
    lzma.decompress(b'x\x9c1\x10\x00\x
