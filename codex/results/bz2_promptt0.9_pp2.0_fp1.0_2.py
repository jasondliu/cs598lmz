import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
input_file = bz2.BZ2File('model_data/data.txt.bz2', 'rb')
text = decompressor.decompress(input_file.read(1024)).decode()

print(text)

decompressor.unused_data = input_file.read(1024)
decompressor.decompress()
decompressor.decompress()

decompressor.decompress('and some more data'.encode('ascii'))

input_file.close()

input_file = bz2.BZ2File('model_data/data.txt.bz2', 'rb')
file_content = input_file.read()
input_file.close()

uncompressed_data_old = decompressor.decompress(file_content)
uncompressed_data_new = bz2.decompress(file_content)
print(uncompressed_data_new.decode())

# Test BZ2File
input_file
