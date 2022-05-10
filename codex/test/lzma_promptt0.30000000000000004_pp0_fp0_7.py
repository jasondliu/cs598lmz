import lzma
# Test LZMADecompressor on a file.

import lzma

with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMADecompressor on a file-like object.

import io
import lzma

with open('test.xz', 'rb') as f:
    compressed_file = io.BytesIO(f.read())

with lzma.open(compressed_file, 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMADecompressor on a file-like object.

import io
import lzma

with open('test.xz', 'rb') as f:
    compressed_file = io.BytesIO(f.read())

with lzma.open(compressed_file, 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMADecompressor on a file-like
