import lzma
lzma.open()
from lzma import LZMAFile
with LZMAFile('foo.txt') as f:
    data = f.read()
from lzma import LZMAFile
with LZMAFile('foo.txt') as f:
    for line in f:
        print(line)
from lzma import LZMAFile
with LZMAFile('foo.txt') as f:
    f.readlines()
from lzma import LZMAFile
with LZMAFile('foo.txt') as f:
    f.readline()
from lzma import LZMAFile
with LZMAFile('foo.txt') as f:
    f.read(8192)
from lzma import LZMAFile
with LZMAFile('foo.txt') as f:
    f.readinto(buf)
from lzma import LZMAFile
with LZMAFile('foo.txt') as f:
    f.readinto1(buf)
from lzma import LZMAFile
with LZMAFile('foo.txt
