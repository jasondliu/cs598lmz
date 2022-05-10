import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print ('Raw data:', data)

decompressor = bz2.BZ2Decompressor()
print ('Decompressed:', decompressor.decompress(data))

try:
    decompressor.decompress(b'garbage')
except OSError as err:
    print ("ERROR:", err)

decompressor = bz2.BZ2Decompressor()
try:
    decompressor.decompress(data)
except OSError as err:
    print ('ERROR:', err)

decompressor.decompress(data[5:])
decompressor.flush()

# Test BZ2Decompress
print (bz2.decompress(data
