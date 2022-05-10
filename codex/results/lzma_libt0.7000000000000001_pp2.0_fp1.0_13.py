import lzma
lzma.open

import lzma
with lzma.open("foo.xz", "rt", encoding="utf-8") as file:
    contents = file.read()

import lzma
with lzma.open("foo.xz", "rb") as file:
    contents = file.read()

import lzma
with lzma.open("foo.xz", "xt") as file:
    file.write("Hello, world!\n")
    file.write("Bye, world!\n")

import lzma
lzma.decompress

import lzma
data = lzma.decompress(b"Hello, world!\n")

import lzma
data = lzma.decompress(b"Hello, world!\n", format=lzma.FORMAT_ALONE)

import lzma
data = lzma.decompress(b"Hello, world!\n")

import lzma
data = lzma.decompress(b"Hello, world!\
