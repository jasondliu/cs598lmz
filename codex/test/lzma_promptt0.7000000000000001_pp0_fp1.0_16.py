import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html
from io import BytesIO

from lzma import LZMADecompressor

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00\x00\x00\x00\x00'

compressor = LZMADecompressor()
with BytesIO(data) as input, BytesIO() as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
