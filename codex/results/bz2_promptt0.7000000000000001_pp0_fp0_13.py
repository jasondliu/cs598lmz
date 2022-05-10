import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
result += decompressor.flush()
print(result)

# Test BZ2File
with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
    with open('lorem.txt', 'rb') as input:
        output.write(input.read())

with bz2.BZ2File('lorem.txt.bz2', 'rb') as f:
    print(f.read())

with bz2.open('lorem.txt.bz2', 'wt') as f:
    f.write
