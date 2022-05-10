import lzma
lzma.LZMACompressor().compress(b"data")

from lzma import LZMAError

try:
    lzma.LZMACompressor().compress(b"data")
except LZMAError as e:
    print(e)
try:
    lzma.LZMADecompressor().decompress(b"data")
except LZMAError as e:
    print(e)
try:
    lzma.LZMADecompressor().decompress(b"")
except lzma.LZMAError as e:
    print(e)

from lzma import LZMAError

try:
    lzma.LZMACompressor().compress(b"data")
except LZMAError as e:
    print(e)
try:
    lzma.LZMADecompressor().decompress(b"data")
except LZMAError as e:
    print(e)
try:
    lzma.LZMADecompressor().decomp
