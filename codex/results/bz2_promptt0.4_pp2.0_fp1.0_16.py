import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

bz_decompressor = bz2.BZ2Decompressor()

try:
    ret = bz_decompressor.decompress(data)
except OSError as e:
    print(e)

print(ret)

# Test BZ2File

with bz2.BZ2File('example.bz2', 'w') as f:
    f.write(b'Hello World!')

with bz2.BZ2File('example.bz2', 'r') as f:
    file_content = f.read()

print(file_content)

# Test compress

uncompressed_data = b'Hello World!Hello World!Hello World
