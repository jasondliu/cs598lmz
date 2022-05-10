import bz2
# Test BZ2Decompressor
text_file = open("input/test.txt", "r")
file_bytes = text_file.read()
text_file.close()

compressed_file = open("input/test.txt.bz2", "wb")
compressor = bz2.BZ2Compressor()
compressed_file.write(compressor.compress(bytes(file_bytes, 'utf-8')))
compressed_file.write(compressor.flush())
compressed_file.close()

decompressed_file = open("input/decompressed_test.txt", "w")
compressed_file = open("input/test.txt.bz2", "rb")
decompressor = bz2.BZ2Decompressor()
for data in iter(lambda : compressed_file.read(100), b''):
    decompressed_file.write(decompressor.decompress(data).decode('utf-8'))
compressed_file.close()
decompressed_file.close()

test_file = open("input/test.txt", "r
