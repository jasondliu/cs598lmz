import lzma
# Test LZMADecompressor

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)

# Error: LZMAError: Input format not supported by decoder
</code>
<code>xz</code> is a compression format that is much more widely used than the <code>lzma</code> format. The <code>xz</code> format is a modernized and improved version of the <code>lzma</code> format.
<code>xz</code> is supported by the <code>lzma</code> module in Python 3:
<code>import lzma
# Test LZMADecompressor

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4
