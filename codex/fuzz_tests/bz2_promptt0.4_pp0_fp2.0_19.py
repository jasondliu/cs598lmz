import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('sample.bz2', 'rb') as f:
    data = f.read(100)
    while data:
        print(decompressor.decompress(data))
        data = f.read(100)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with bz2.open('sample.bz2', 'wb') as f:
    f.write(compressor.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
    f.write(compressor.compress(b'hello'))
    f.write(compressor.flush())
 
# Test BZ2File

with
