import lzma
# Test LZMADecompressor

import io
import lzma

# Create a buffer containing compressed data
compressed = io.BytesIO()
with lzma.open(compressed, "w") as f:
    f.write(b"Hello, world!\n")

# Read the compressed data from the buffer
compressed.seek(0)
with lzma.open(compressed) as f:
    print(f.read())

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one chunk of compressed data at a time
compressed.seek(0)
while True:
    chunk = compressed.read(1024)
    if not chunk:
        break
    data = decompressor.decompress(chunk)
    if data:
        print(data)

# Finish decompression
data = decompressor.flush()
print(data)
# Test LZMAFile

import lzma

with lzma.open("test.xz", "wt") as f:
    f.write("Hello, world!\n
