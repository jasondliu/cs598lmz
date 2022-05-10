import lzma
# Test LZMADecompressor
from lzma import LZMADecompressor
from io import BytesIO

compressor = LZMADecompressor()
with open('foo.xz', 'rb') as input:
    with open('foo.out', 'wb') as output:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
