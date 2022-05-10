import bz2
# Test BZ2Decompressor object on a file piece by piece.
decompressor = bz2.BZ2Decompressor()
compressed_data = open("somefile.bz2", "rb").read()
data = decompressor.decompress(compressed_data)
print(len(data))

print(repr(data[:20]))
# Test BZ2Decompressor object on a file one chunk at a time.
decompressor = bz2.BZ2Decompressor()
compressed_file = open("somefile.bz2", "rb")
chunk = compressed_file.read(100)
while chunk:
    data = decompressor.decompress(chunk)
    if data:
        print(len(data))
    chunk = compressed_file.read(100)
    print("Done")

print(type(data))
# The bz2 module provides a very easy-to-use interface for compressing
# and decompressing data.
import bz2
for i in range(1, 10):
    s = b"Hello world! " * i
   
