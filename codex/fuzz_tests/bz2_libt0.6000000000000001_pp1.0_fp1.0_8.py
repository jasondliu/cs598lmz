import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import bz2
bz2.compress(b'Hello World')

import bz2
bz2.BZ2Compressor().compress(b'Hello World')

import bz2
bz2.BZ2Compressor().flush()

import bz2
bz2.BZ2Decompressor().decompress(bz2.compress(b'Hello World'))

import bz2
bz2.BZ2Decompressor().flush()

import bz2
bz2.open('file.txt', mode='wt')

import bz2
bz2.open('file.txt.bz2', mode='wt')

import bz2
bz2.open('file.txt.bz2', mode='wt', compresslevel=9)

import bz2
bz2.open('file.txt.bz2', mode='wt', encoding='utf-8')

import bz2
bz2.open
