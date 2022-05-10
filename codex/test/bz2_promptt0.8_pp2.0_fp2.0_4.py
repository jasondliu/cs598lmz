import bz2
# Test BZ2Decompressor

print("Type 'quit' to exit.")

d = bz2.BZ2Decompressor()

while True:
    data = input("Enter data to decompress: ")
    if not data:
        continue

    if data == "quit":
        break

    print("Decompressed:", d.decompress(data.encode("ascii")).decode("ascii"))

# Test BZ2Compressor

print("Type 'quit' to exit.")

c = bz2.BZ2Compressor()

while True:
    data = input("Enter data to compress: ")
    if not data:
        continue

    if data == "quit":
        break

    print("Compressed:", c.compress(data.encode("ascii")).decode("ascii"))

import bz2

