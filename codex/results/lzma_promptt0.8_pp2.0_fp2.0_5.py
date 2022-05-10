import lzma
# Test LZMADecompressor
with lzma.open("wikipedia.xml.xz", "rb") as f:
    file_content = f.read()
    print(file_content)

import lzma
# Building a LZMA compressed file
with lzma.open('blah.xz', 'w') as f:
    f.write(b"Some random data")

import lzma
# Inspecting the attributes of an LZMA file
import lzma

with lzma.open('example.xml.xz', 'rb') as f:
    print(f.fileno())
    print(f.seekable())
    print(f.readable())
    print(f.writable())
    print(f.name)

import lzma
# Inspecting the attributes of an LZMA file
import lzma

with lzma.open('example.xml.xz', 'rb') as f:
    print(f.fileno())
    print(f.seekable())
    print(f.readable())
    print(f.writable())
   
