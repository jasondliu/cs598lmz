import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decompressor = BZ2Decompressor()

result = decompressor.decompress(data)
result += decompressor.flush()

print(result)

# Test BZ2File

bz = bz2.BZ2File('file.bz2')
try:
    for line in bz:
        print(line.strip())
finally:
    bz.close()


with bz2.BZ2File('file.bz2') as bz:
    for line in bz:
        print(line.strip())

# Using with statement to compress a file

with bz2.BZ2File('compressed.txt.bz2', 'w') as
