import lzma
# Test LZMADecompressor
uncomp = lzma.LZMADecompressor()
res = uncomp.decompress(c)
print(res)
print(len(res))
 
# Test LZMACompressor
comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE,
                           check=-1, preset=9)
res = comp.compress(b'The quick brown fox jumps over the lazy dog.')
res += comp.flush()
# res should be same as c
print(res==c)

decomp = lzma.LZMADecompressor()
res = decomp.decompress(res)
print(res)


# Test XZ Filter styles
print("STDIO_VERSION", lzma.STDIO_VERSION)
print("FORMAT_ALONE", lzma.FORMAT_ALONE)
print("FORMAT_XZ", lzma.FORMAT_XZ)
print("CHECK_NONE", lzma.CHECK_NONE)
print("CHECK_CRC32", lzma.CHECK_
