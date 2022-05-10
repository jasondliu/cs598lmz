import bz2
# Test BZ2Decompressor

compressed_data = bz2.compress(b"This is a test")
print(compressed_data)

decompressor = bz2.BZ2Decompressor()

try:
    data = decompressor.decompress(compressed_data)

except EOFError:
    print("The end of the compressed data stream has been reached")

print(data)

# BZ2File

with bz2.BZ2File("compressed_text.bz2", "wb") as output:
    for line in open("lorem_ipsum.txt", "rt"):
        output.write(line.encode("utf-8"))

with bz2.BZ2File("compressed_text.bz2", "rb") as input:
    for line in input:
        print(line.decode("utf-8"))

# zlib

import zlib

data = b"The quick brown fox jumped over the lazy dog."

compressed = zlib.compress(data)
print(compressed)


