import bz2
# Test BZ2Decompressor

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressed = bz2.compress(un)
with open('io\\bz2compressed.bz2', 'wb') as f:
    f.write(compressed)

decompressor = bz2.BZ2Decompressor()
with open('io\\bz2compressed.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

    

with bz2.open('io\\bz2compressed.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)
