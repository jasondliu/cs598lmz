from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# LZMA/XZ compressed data

import lzma
import io

buf = io.BytesIO(data)
f = lzma.open(buf)
f.read()

# bzip2 compressed data

import bz2
bz2.decompress(data)

# bzip2 compressed data

import bz2
import io

buf = io.BytesIO(data)
f = bz2.BZ2File(buf)
f.read()

# Pack200

import io
import lzma
import pack200

buf = io.BytesIO(data)
f = lzma.LZMAFile(buf)
p = pack200.Unpacker()
p.unpack(f)

# Pack200

import io
import pack200

buf = io.BytesIO(data)
f = pack200.open(buf)
f.read()

# DEFLATE compressed data

import zlib
zlib.decompress(data, -zlib.MAX_W
