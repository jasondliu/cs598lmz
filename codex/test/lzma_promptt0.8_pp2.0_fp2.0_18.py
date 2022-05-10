import lzma
# Test LZMADecompressor as a decompression object.
inp = b'\x00' * 100 + lzma.LZMACompressor().compress(b'junkjunk')
inp += lzma.LZMACompressor().flush()

c = lzma.LZMADecompressor()
outp = []
ret = c.decompress(inp, 25)
outp.append(ret)
