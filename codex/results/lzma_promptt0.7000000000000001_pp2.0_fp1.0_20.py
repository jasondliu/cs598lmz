import lzma
# Test LZMADecompressor
lzdec = lzma.LZMADecompressor()

out = lzdec.decompress(hexcompressed)
print(out)

# Test BZ2Compressor
bcomp = bz2.BZ2Compressor()

bcomp.compress(b"This is a test")
bcomp.flush()

# Test BZ2Decompressor

bdec = bz2.BZ2Decompressor()

bdec.decompress(hexcompressed2)
bdec.flush()

# Test ZlibCompressor
zcomp = zlib.compressobj()

zcomp.compress(b"This is a test")
zcomp.flush()

# Test ZlibDecompressor
zdec = zlib.decompressobj()

zdec.decompress(hexcompressed2)
zdec.flush()

# Test ZstdCompressor
zcom = zstd.ZstdCompressor()

zcom.compress(b"This is a test")
zcom.flush()

# Test Zstd
