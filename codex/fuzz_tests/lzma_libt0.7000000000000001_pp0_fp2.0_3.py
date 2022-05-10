import lzma
lzma_check_values = [
    lzma.CHECK_CRC32,
    lzma.CHECK_CRC64,
    lzma.CHECK_NONE,
]

import hashlib
hash_values = [
    hashlib.md5(),
    hashlib.sha1(),
    hashlib.sha224(),
    hashlib.sha256(),
    hashlib.sha384(),
    hashlib.sha512(),
]

import zlib
zlib_values = [
    zlib.Z_BEST_COMPRESSION,
    zlib.Z_BEST_SPEED,
    zlib.Z_DEFAULT_COMPRESSION,
    zlib.Z_HUFFMAN_ONLY,
    zlib.Z_NO_COMPRESSION,
]

import bz2
bz2_values = [
    bz2.BZ2_FILTERED,
    bz2.BZ2_HUFFMAN_ONLY,
    bz2.BZ2_RLE,
    bz2.BZ2_
