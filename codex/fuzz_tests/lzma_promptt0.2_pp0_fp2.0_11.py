import lzma
# Test LZMADecompressor

# Test that the decompressor can decompress a file compressed with the
# reference implementation.

# The file was compressed with the following command:
# xz -z -k -9 -e -b 1k testdata/lorem.txt

# The file was compressed with the following command:
# xz -z -k -9 -e -b 1k testdata/lorem.txt

with open('testdata/lorem.txt.xz', 'rb') as f:
    data = f.read()

d = lzma.LZMADecompressor()

# Decompress the whole file at once
decompressed = d.decompress(data)

# Decompress the file in chunks
decompressed = b''
while True:
    chunk = d.decompress(data)
    if not chunk:
        break
    decompressed += chunk

# Decompress the file in chunks, with a different chunk size
decompressed = b''
while True:
    chunk = d.decompress(data, 1024)
    if not chunk:
