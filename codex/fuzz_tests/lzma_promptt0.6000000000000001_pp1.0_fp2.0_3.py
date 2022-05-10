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
            output.write(compressor.decompress(chunk))
        output.write(compressor.flush())
# Test LZMAFile
from lzma import LZMAFile
with LZMAFile('foo.xz', 'r') as input:
    with open('foo.out', 'wb') as output:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            output.write(chunk)

# Test LZMAError
from lzma import LZMAError
try:
    LZMAFile('foo.xz', 'w')
except LZMAError as e:
    print(e)

# Test LZMAFile
