import bz2
# Test BZ2Decompressor
# The original example used ASCII codes instead of characters.
# I have modified it to use characters.

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
output = result.decode('ascii')
print(output)

print(bz2.decompress(data))
# Test BZ2Compressor

data = 'This is a Test!'
compressor = bz2.BZ2Compressor()
result = compressor.compress(data.encode('ascii'))
result += compressor.flush()

print(result)
print(bz2.compress(data.encode('ascii')))
 

# Test
