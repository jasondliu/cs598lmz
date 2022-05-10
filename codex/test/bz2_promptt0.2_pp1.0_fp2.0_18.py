import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decompressor = bz2.BZ2Decompressor()

decompressed_data = decompressor.decompress(data)

print(decompressed_data)

# Test BZ2File

with bz2.BZ2File('lorem.txt.bz2') as input:
    print(input.read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

