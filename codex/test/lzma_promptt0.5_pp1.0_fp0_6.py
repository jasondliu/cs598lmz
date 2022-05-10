import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
data = open('test.xz', 'rb').read()
decompressor.decompress(data)
# decompressor.decompress(b"")

# print(decompressor.unused_data)
print(decompressor.eof)

# print(lzma.decompress(data))

import lzma

with lzma.open('test.xz') as f:
    file_content = f.read()

print(file_content)

import lzma

with lzma.open('test.xz', mode='rt') as f:
    file_content = f.read()

print(file_content)

import lzma

with lzma.open('test.xz', mode='wt') as f:
    f.write('hello world\n')

import lzma

