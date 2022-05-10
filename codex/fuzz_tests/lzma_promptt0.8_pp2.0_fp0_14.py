import lzma
# Test LZMADecompressor

msg = b'Blah blah blah Looks like this is a non-compressed string. Blah blah blah'

c = lzma.LZMADecompressor()
c.decompress(msg, max_length=100)
# Test LZMADecompressor

msg = b'Blah blah blah Looks like this is a non-compressed string. Blah blah blah'

c = lzma.LZMACompressor()
c.decompress(msg)
# Test LZMADecompressor

msg = b'Blah blah blah Looks like this is a non-compressed string. Blah blah blah'

c = lzma.LZMADecompressor()
c.decompress(msg, max_length=100)
# Test LZMADecompressor

msg = b'Blah blah blah Looks like this is a non-compressed string. Blah blah blah'

c = lzma.LZMACompressor()
c.decompress(msg)
c.flush()
# Test LZMADecomp
