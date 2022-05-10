from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data) == original_data

from zlib import decompress
decompress(zlib_data) == original_data

import zlib
decompressobj = zlib.decompressobj()
decompressobj.decompress(zlib_data) == original_data
decompressobj.flush() == b""


# Encode binary data with Base64
import base64
base64.b64encode(b"binary\x00data")
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64decode(b'abcd--__')


# Decode/encode with ASCII85
import base64
from binascii import a2b_base64, b2a_base64

# Convert a binary string to BASE64.
b2a_base64(b"binary\x00data
