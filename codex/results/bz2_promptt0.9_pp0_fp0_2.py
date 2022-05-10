import bz2
# Test BZ2Decompressor
data = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes long'.format(len(data)))

decompressed = bz2.decompress(data)
print('Output is {} bytes long'.format(len(decompressed)))
print(decompressed)
 
# Test BZ2Compressor
compressed = bz2.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\r\r\rK\rK\rE\rE\r\x94\r\x94\x8cl \x00!\x9ah3M\x07<]\xc9\x14)\x81m\x91\xb2\x0
