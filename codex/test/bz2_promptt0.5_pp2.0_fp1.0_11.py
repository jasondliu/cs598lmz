import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('test.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(decompressor.decompress(file_content))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

uncompressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressed_data = compressor.compress(uncompressed_data)
final_data = compressed_data + compressor.flush()

print(final_data)

# BZ2File

