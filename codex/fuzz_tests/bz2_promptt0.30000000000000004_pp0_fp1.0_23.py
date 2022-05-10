import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is %d bytes' % len(data))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Output is %d bytes' % len(result))
print(result)

print('Total input is %d bytes' % len(data))
print('Total output is %d bytes' % len(result))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
result = compressor.compress(data)
result += compressor.flush()
print('Output is %d bytes' % len(result))

print('Total input is %d bytes' % len(data))
print('Total output is %d bytes
