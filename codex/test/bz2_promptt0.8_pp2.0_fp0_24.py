import bz2
# Test BZ2Decompressor
source = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('source:', source)

# BZ2Decompressor.__init__() 
decompressor = bz2.BZ2Decompressor()
try:
    # BZ2Decompressor.decompress() 
    data = decompressor.decompress(source)
except EOFError:
    # BZ2Decompressor.unused_data 
    unused_data = decompressor.unused_data
print('unused_data:', decompressor.unused_data)
print('data:', data)
print('Decompressed', len(data), 'bytes.')
