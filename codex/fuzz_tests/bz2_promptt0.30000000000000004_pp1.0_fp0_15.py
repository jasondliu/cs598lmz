import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print(result)
print(len(result))

# Test BZ2File
with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(block)

# Test compress
with open('lorem.txt', 'rb') as input:
    data = input.read()
    compressed = bz2.compress(data)

