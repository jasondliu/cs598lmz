import lzma
# Test LZMADecompressor
s = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
d = lzma.LZMADecompressor()
data = d.decompress(s)
print(data)
data += d.flush()
# Test LZMACompressor
c = lzma.LZMACompressor()
new_s = c.compress(data)
print(new_s)
new_s += c.flush()
print(new_s)
print(d.decompress(new_s))
print(d.flush())
</code>
Result
<code>b'HELLO\n'
b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00
