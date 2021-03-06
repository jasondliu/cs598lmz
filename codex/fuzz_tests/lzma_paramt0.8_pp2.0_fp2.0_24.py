from lzma import LZMADecompressor
LZMADecompressor().decompress(base64.b64decode(src_lzma))

import numpy as np
import lzma

x = np.ones((10, 10))
data = lzma.compress(x.tobytes())

print(data)
# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x04\xd3\xcd\xcf\x07\x00\x00\x00'

print(type(data))
# <class 'bytes'>

print(lzma.decompress(data))
# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
