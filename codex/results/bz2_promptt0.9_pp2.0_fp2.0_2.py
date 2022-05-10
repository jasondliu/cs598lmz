import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes, compressed'.format(len(data)))
decomp = bz2.BZ2Decompressor()
result = decomp.decompress(data)
print('Output is {} bytes'.format(len(result)))
print(result)


# Test BZ2Compressor
data = b'This is the original text.'
print('Input :', data)
comp = bz2.BZ2Compressor()
result = comp.compress(data) + comp.flush()
print('Output is {} bytes'.format(len(result)))
decomp = bz2.BZ2Decompressor()
out = decomp.decompress(result)
print('Decompressed:', out)

# Test B
