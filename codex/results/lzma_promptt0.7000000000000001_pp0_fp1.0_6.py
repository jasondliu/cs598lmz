import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)

import pickle
# Test Pickler
pickle.dumps(object)

import cPickle
# Test Pickler
cPickle.dumps(object)

import zlib
# Test Compress
zlib.compress(data)

import zlib
# Test Decompress
zlib.decompress(data)

import zlib
# Test CRC32
zlib.crc32(data)

import hashlib
# Test MD5
hashlib.md5(data)

import hashlib
# Test SHA1
hashlib.sha1(data)

import hashlib
# Test SHA224
hashlib.sha224(data)

import hashlib
# Test SHA256
hashlib.sha256(data)

import hashlib
# Test SHA384
hashlib.sha384(data)

import hashlib
# Test SHA512
hashlib.sha512(data)

import hashlib
# Test SHA3_224
hash
