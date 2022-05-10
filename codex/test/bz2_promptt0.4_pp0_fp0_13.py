import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is %d bytes' % len(data))
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Output is %d bytes' % len(result))
print(result)

print('-'*20)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
result = compressor.compress(b'This is the first part of the data. ')
print('Output is %d bytes' % len(result))
result += compressor.compress(b'And this is the second part. ')
print('Output is %d bytes' % len(result))
