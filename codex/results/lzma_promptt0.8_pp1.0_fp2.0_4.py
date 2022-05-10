import lzma
# Test LZMADecompressor
c = LZMADecompressor()
for data in [b"", b"a", b"ab", b"abc", b"abcd"]:
    c.decompress(data)
# Test LZMADecompressor.flush()
c = LZMADecompressor()
c.decompress(b"abcd")
for data in [b"", b"a", b"ab", b"abc", b"abcd"]:
    c.flush()
# Test LZMADecompressor's buffer_size
cmp = bz2.BZ2Compressor()
cmprsd = cmp.compress(b"abcdefgh" * 1024)
cmprsd += cmp.flush()

decomp = lzma.LZMADecompressor()
for length in range(1, 9):
    data = b""
    for start in range(0, len(cmprsd), length):
        data += decomp.decompress(cmprsd[start:start + length])
    data += decomp.flush()
    if data != b
