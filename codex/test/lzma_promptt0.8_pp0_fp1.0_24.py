import lzma
# Test LZMADecompressor
 
comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
with open('/dev/null', 'wb') as fnull:
    comp.compress(b'12345678')
