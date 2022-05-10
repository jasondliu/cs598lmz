import lzma
# Test LZMADecompressor as a decompression object.
inp = b'\x00' * 100 + lzma.LZMACompressor().compress(b'junkjunk')
inp += lzma.LZMACompressor().flush()

c = lzma.LZMADecompressor()
outp = []
ret = c.decompress(inp, 25)
outp.append(ret)
ret = c.decompress(inp)
outp.append(ret)
if outp != [b'junkjunk', b'']:
    raise AssertionError
import lzma
# Test incremental compression.
comp = lzma.LZMACompressor()
data = b'this is the data to compress'
ret = comp.compress(data)
ret += comp.flush()
ret += comp.compress(b'and this is more data')
ret += comp.flush()
import lzma
# Test incremental decompression.
decomp = lzma.LZMADecompressor()
data = b'this is the data to decompress
