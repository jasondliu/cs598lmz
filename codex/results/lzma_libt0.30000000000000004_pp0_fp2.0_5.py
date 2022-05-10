import lzma
lzma.LZMAFile

import lzma

with lzma.open("foo.xz", "wt") as f:
    f.write("Hello, world!\n")

with lzma.open("foo.xz") as f:
    print(f.read())

import lzma

with lzma.open("foo.xz", "rt") as f:
    print(f.read())

import lzma

with lzma.open("foo.xz", "rt") as f:
    for line in f:
        print(line)

import lzma

with lzma.open("foo.xz", "rt") as f:
    print(f.readline())

import lzma

with lzma.open("foo.xz", "rt") as f:
    print(f.readlines())

import lzma

with lzma.open("foo.xz", "rt") as f:
    print(f.read(10))

import lzma
