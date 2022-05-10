import lzma
# Test LZMADecompressor

msg = b'Blah blah blah Looks like this is a non-compressed string. Blah blah blah'

c = lzma.LZMADecompressor()
