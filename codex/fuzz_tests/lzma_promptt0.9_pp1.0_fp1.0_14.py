import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
l = d.decompress(b"x\x9cK\xcb\xcf\x07\x00\x02\x82\x04KL\x85\xccH\xcbE\xa2\xe2\x02\x00D\x1c\x00\x00\x00\x00")
print(l)
</code>
<code>b'This is written in Python.\n'
</code>
So it works, albeit with a slight modification. 

