import lzma
lzma.open

import lzma
with lzma.open("foo.xz", "rt", encoding="utf-8") as file:
    contents = file.read()

import lzma
with lzma.open("foo.xz", "rb") as file:
    contents = file.read()

import lzma
