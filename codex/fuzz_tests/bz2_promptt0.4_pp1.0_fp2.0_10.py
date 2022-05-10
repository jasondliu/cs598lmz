import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

uncompressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressed_data = compressor.compress(uncompressed_data) + compressor.flush()

print(compressed_data)

# Test BZ2File

with bz2.open('sample.bz2', 'rt') as f:
    file_content = f.read()
    print(file_content)

# Test B
