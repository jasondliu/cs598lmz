import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
c.decompress(S1[:15])
# Test LZMAEncoder
c = lzma.LZMAEncoder()
c.compress(S1)
c.checksum()
# Test LZMADecompressor
c = lzma.LZMADecompressor()
c.decompress(S2)
# Test LZMAEncoder
c = lzma.LZMAEncoder()
c.compress(S2)
c.checksum()
# Test LZMADecompressor
c = lzma.LZMADecompressor()
c.decompress(S1[:15]+S2)
# Test LZMAEncoder
c = lzma.LZMAEncoder()
c.compress(S1+S2)
c.checksum()
# Test overrun after decompression
# When decompressed data longer than 3kb was passed to LZMADecompressor,
# it caused a buffer overrun when it was freed, leading
