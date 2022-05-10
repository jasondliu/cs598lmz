import lzma
# Test LZMADecompressorClass .decompress()
dobj = lzma.LZMADecompressor()
assert_raises(TypeError, dobj.decompress)
# Test LZMADecompressorClass .decompress() with various invalid input types
dobj = lzma.LZMADecompressor()
for _in in ([], True, None, "", (), set(), {}, frozenset(), 1, 1.1, object()):
    assert_raises(TypeError, dobj.decompress, _in)

# Test LZMADecompressorClass .decompress() with no initial data
dobj = lzma.LZMADecompressor()
assert_equal(dobj.decompress(b""), b"")
# Test LZMADecompressorClass .decompress() with valid input
dobj = lzma.LZMADecompressor()
dobj.decompress(COMPRESSED_TEXT)
assert_equal(dobj.unused_data, b"")
# Test LZMADecompressor
