import lzma
# Test LZMADecompressor.

# Create a decompressor object.
decompressor = lzma.LZMADecompressor()

# Decompress data from one file object using another file object.
with open('lorem.xz', 'rb') as input, \
     open('lorem-decompressed', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Decompress data from a file-like object.
with open('lorem.xz', 'rb') as input:
    data = decompressor.decompress(input.read())

# Decompress data from a bytes object.
data = decompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04]\xfd
