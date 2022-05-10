import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

try:
    f = bz2.open('bz2_file.txt', 'wb')
except IOError:
    print("File not found or path is incorrect")

f.write(b'This is a test')
f.close()

f = bz2.open('bz2_file.txt', 'rb')
decompressed_data = decompressor.decompress(f.read())
decompressed_data += decompressor.flush()
f.close()

print(decompressed_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

f = bz2.open('bz2_file_compressed.txt', 'wb')

f.write(compressor.compress(b'This is a test'))
f.write(compressor.flush())
f.close()

f = bz2.open('bz2_file_compressed.txt', 'rb')
compressed_data =
