import bz2
# Test BZ2Decompressor and BZ2Compressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))
compressor = bz2.BZ2Compressor()
ret = compressor.compress(data)
ret += compressor.flush()
print(len(ret))
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(ret))
print(decompressor.unused_data)

# Test BZ2File
print("BZ2File")
with bz2.BZ2File('file.bz2', 'w') as bz2_file:
    bz2_file.write(b'Hello World')
