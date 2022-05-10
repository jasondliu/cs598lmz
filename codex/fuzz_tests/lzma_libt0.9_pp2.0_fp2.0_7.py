import lzma
lzma.LZMADecompressor()(b'\x00').decode()
# 'parser' object has no attribute 'LZMADecompressor'


c = lzma.LZMACompressor()
b = c.compress(b'abc')
b += c.flush()
l = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
l.decompress(b)

# 'parser' object has no attribute 'FORMAT_RAW'
</code>
It's not working at all. It is turning bad a good string.
Where is my error? I am out of ideas.
Can someone help me?
P.S: I need to convert the output of this in str, not in bytes.

