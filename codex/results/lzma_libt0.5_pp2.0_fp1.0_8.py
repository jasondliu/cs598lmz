import lzma
lzma.LZMAFile

import lzma
import os.path

# Get the name of the file we want to create.
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "x.xz"

# Create a file with some data to compress.
with open(filename, "wb") as f:
    f.write(b"Hello")

# Compress the file.
with lzma.open(filename + ".xz", "w") as f:
    f.write(open(filename, "rb").read())

# Decompress the file.
with lzma.open(filename + ".xz") as f:
    file_content = f.read()

# Verify that the decompression gave us the original data back.
assert file_content == b"Hello"

# Clean up the original file.
os.remove(filename)

# Clean up the compressed file.
os.remove(filename + ".xz")
