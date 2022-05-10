import lzma
# Test LZMADecompressor
with lzma.open("test_1.xz") as fi:
    data = fi.read()
data

from lzma import LZMADecompressor
d = LZMADecompressor()
d.decompress(data)

from lzma import LZMADecompressor
from io import BytesIO

with lzma.open("test_1.xz") as fi:
    d = LZMADecompressor()
    fo = BytesIO()

    while True:
        block = fi.read(1024)
        if not block:
            break
        fo.write(d.decompress(block))

    fo.seek(0)
    print(fo.read())
 
    fo.close()
 
# Test LZMAFile
with lzma.open("test_1.xz") as fi:
    print(fi.read())
 
with lzma.open("test_1.xz") as fi:
    while True:
        block = fi.read(1024)
       
