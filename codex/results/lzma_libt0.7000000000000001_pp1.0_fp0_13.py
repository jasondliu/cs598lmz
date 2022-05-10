import lzma
lzma.LZMAFile

import lzma

# Open a file in read mode
with lzma.open("compress.py.xz", "r") as file:
    file_content = file.read()
    print(file_content)

# Open a file in write mode
with lzma.open("compress.py.xz", "w") as file:
    file.write("Hello world!")

# Open a file in append mode
with lzma.open("new.txt.xz", "a") as file:
    file.write("Hello world!")

import lzma

# Compress data
data = b"Hello world!"
with lzma.open("compressed_file", "w") as f:
    f.write(data)

# Decompress data
with lzma.open("compressed_file") as f:
    file_content = f.read()
    print(file_content)
