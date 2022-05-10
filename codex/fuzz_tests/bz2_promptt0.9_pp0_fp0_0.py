import bz2
# Test BZ2Decompressor
with open ('test_compressed_file.bz2','rb') as test_file:
    data=test_file.read()
    test_compressed=bz2.BZ2Decompressor()
    decompressed=test_compressed.decompress(data)
    with open ('test_decompressed_file.txt','wb') as txt_file:
        txt_file.write(decompressed)
with open ('test_decompressed_file.txt') as txt_file:
    print(txt_file.read())

# Test BZ2Compressor
with bz2.BZ2Compressor() as test_compressor:
    with open ('test_file.txt', 'rb') as test_file:
        data=test_file.read()
        compressed=test_compressor.compress(data)
with open ('test_compressed_file.bz2', 'wb') as bz2_file:
    bz2_file.write(compressed)

# Test open fn as context manager
with bz2.open
