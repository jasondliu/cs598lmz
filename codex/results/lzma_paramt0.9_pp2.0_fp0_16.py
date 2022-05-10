from lzma import LZMADecompressor
LZMADecompressor.check(b'\x00', 0)

from xattr import xattr
xattr.xattr()
xattr.get(b'filename')
xattr.set(b'filename')
xattr.list(b'filename')
xattr.remove(b'filename')

from zlib import decompress, compress
decompress(b'\x00')
compress(b'\x00')

import _json
_json.dump(b"\u1234")
_json.dumps(b"\u1234")

import _pickle
_pickle.loads(b"\\x00 ")

# The struct module will always take bytes, bytestring or buffer
import struct
struct.pack(b"!L", 123)
struct.unpack(b"!L", b"\x7b")

# The sys module always uses bytes in C/C++ filenames
import sys
sys.getwindowsversion().encode()

# The ElementTree module always takes bytestring or buffer
import xml.etree.expat
with XMLParser() as parser
