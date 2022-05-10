import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"Some data")
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)
decompressor.flush()

# Test LZMAFile
with lzma.LZMAFile(("case.1.lzma", "rb")) as cfile:
    for line in cfile:
        pass
with lzma.LZMAFile(("case.1.lzma", "rb"), format=lzma.FORMAT_XZ) as cfile:
    for line in cfile:
        pass
with lzma.LZMAFile(("case.1.lzma", "rb"), check=-1) as cfile:
    for line in cfile:
        pass
with lzma.LZMAFile(("case.1.lzma", "rb"), format=lzma.FORMAT_ALONE) as cfile:
    for line in cfile
