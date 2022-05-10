from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

from lzma import LZMAError
try:
    LZMADecompressor().decompress(compressed_data)
except LZMAError:
    print("Compressed data stream is corrupt")

from lzma import LZMAError
try:
    LZMADecompressor().decompress(b"garbage")
except LZMAError:
    print("Compressed data stream is corrupt")

import lzma
with lzma.open("file.xz") as f:
    file_content = f.read()

import lzma
with lzma.open("file.xz", mode="rt") as f:
    file_content = f.read()

import lzma
with lzma.open("file.xz", mode="wt") as f:
    f.write(text)

import lzma
with lzma.open("file.xz", mode="ab") as f:
    f.write(data)

import lzma
with
