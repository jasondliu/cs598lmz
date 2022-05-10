import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

data = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"

more = decompressor.decompress(data)

print(more)

# Test BZ2File

with bz2.BZ2File('sample.bz2') as f:
    print(f.read())

# Test compress

data = b"Hello, World!"

compressed = bz2.compress(data)

print(compressed)

# Test decompress

compressed = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x
