import lzma
# Test LZMADecompressor

import lzma

with lzma.open('data/python.xz') as f:
    file_content = f.read()

print(file_content[:10])

compressor = lzma.LZMACompressor()

with open('data/python.xz', 'rb') as input, \
        open('data/uncompressed.txt', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

with open('data/uncompressed.txt', 'rb') as f:
    file_content = f.read()

print(file_content[:10])

# Test LZMAFile

import lzma

with lzma.open('data/python.xz') as f:
    file_content = f.read()

print(file_content[:10])

with open('data
