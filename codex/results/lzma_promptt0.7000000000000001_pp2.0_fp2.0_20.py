import lzma
# Test LZMADecompressor.__repr__()
with lzma.open(BytesIO(b"\xfd7zXZ\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00")) as compressor:
    assert repr(compressor) == "<lzma.LZMADecompressor object at 0x{0:x}>".format(
        id(compressor))
    compressor.decompress(b"\x00")
    assert repr(compressor) == "<lzma.LZMADecompressor object at 0x{0:x} (finished)>".format(
        id(compressor))

# Test LZMAFile.__init__()
