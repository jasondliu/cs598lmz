import lzma
# Test LZMADecompressor with a dictionary
comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE, filters=[lzma.FILTER_LZMA2, {'id': lzma.FILTER_LZMA2, 'dict_size': 2**16}])
cdata = comp.compress(b'Hello')
cdata += comp.compress(b' World')
cdata += comp.flush()
print(cdata)

decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE, filters=[lzma.FILTER_LZMA2, {'id': lzma.FILTER_LZMA2, 'dict_size': 2**16}])
print(decomp.decompress(cdata))
print(decomp.decompress(b''))

print(decomp.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'*10))
print(decomp.decompress
