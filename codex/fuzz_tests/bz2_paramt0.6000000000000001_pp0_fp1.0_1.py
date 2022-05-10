from bz2 import BZ2Decompressor
BZ2Decompressor()

from base64 import b64decode
b64decode("YWJjZA==")

from pbkdf2 import PBKDF2
pbkdf2 = PBKDF2("password", salt="salt")
pbkdf2.read(1000)

from bcrypt import bcrypt
bcrypt("password")

from lzma import compress, decompress
compress("hello world")
decompress(compress("hello world"))

from lzma import LZMACompressor, LZMADecompressor
LZMACompressor().compress("hello world")
LZMADecompressor().decompress(LZMACompressor().compress("hello world"))

from zlib import compress, decompress
compress("hello world")
decompress(compress("hello world"))

from zlib import compress, decompress
compress("hello world")
decompress(compress("hello world"))

import zlib
zlib.compress("hello world")
zlib.decompress(zlib.compress("hello world"))


