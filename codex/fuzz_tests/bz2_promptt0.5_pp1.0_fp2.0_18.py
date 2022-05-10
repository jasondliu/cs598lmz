import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decomp = bz2.BZ2Decompressor()
print(decomp.decompress(data))
print(decomp.decompress(b'\x00\x00\x00\x00\x00\x01\x01BZ'))
print(decomp.flush())

# decompress a file
# with open('file.bz2', 'rb') as f:
#     print(decomp.decompress(f.read()))

# decompress a stream
# decomp = bz2.BZ2Decompressor()
# with open('file.bz2', 'rb') as f:
#     for data in iter(lambda: f.read(100), b''
