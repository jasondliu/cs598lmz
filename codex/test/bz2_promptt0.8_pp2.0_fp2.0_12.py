import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()

print('Decompressed is {} bytes'.format(decompressor.decompress(data)))

print('Remainder is {} bytes'.format(decompressor.unused_data))

# bz2.decompress is a shortcut for creating a decompressor and calling its decompress() method
print('Shortcut result is {} bytes'.format(bz2.decompress(data)))

