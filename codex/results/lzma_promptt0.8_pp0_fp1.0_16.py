import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
#lzma.decompress(data)
with lzma.open('lfs-data.7z') as f:
    file_content = f.read()
    print(file_content)

for data in file_content:
    uncompressed += compressor.decompress(data) # add more data to the decompressor, 
                                                 # and get some more decompressed data
    if compressor.unused_data:
        break # we've finished decompressing
print(uncompressed)
with lzma.open('my_new_file.txt', mode='w') as f:
    f.write(uncompressed)

compressed = lzma.compress(uncompressed)
print(compressed)

with lzma.open('my_new_file_compressed.txt', mode='w') as f:
    f.write(compressed)

with lzma.open('my_new_file_compressed.txt') as f:
    file_content = f
