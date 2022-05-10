import bz2
# Test BZ2Decompressor without starting newlines
compressor = bz2.BZ2Compressor(9)
data = b"a"
compressor.compress(data)
bz2data = compressor.flush()
decompressor = bz2.BZ2Decompressor()

try:
    decompressor.decompress(bz2data)
except EOFError as e:
    assert isinstance(e.args[0], str)
    assert e.args[0].startswith("BZ2Decompressor")
    assert e.args[0].endswith("decompression OK, so far.")
