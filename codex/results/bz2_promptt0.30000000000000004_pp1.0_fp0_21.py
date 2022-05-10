import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('data/compressed.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
with open('data/compressed.bz2', 'wb') as f:
    f.write(compressor.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
    f.write(compressor.flush())

# Test BZ2File
with bz2.BZ2File('data/compressed.bz2', 'wb') as f:
    f.write(b'Hello World!')


