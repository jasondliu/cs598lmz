from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00')

import lzma
lzma.open('file.xz')
lzma.open('file.xz', mode='wt')

import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write('Hello World!')

import lzma
with lzma.open('file.xz', 'rt') as f:
    text = f.read()

import lzma
with lzma.open('file.xz', 'rt') as f:
    for line in f:
        print(line)

import lzma
with lzma.open('file.xz', 'rt') as f:
    text = f.read()
    print(text)

import lzma
with lzma.open('file.xz', 'rt') as f:
    print(f.readline())

import lzma
with lzma.open('file
