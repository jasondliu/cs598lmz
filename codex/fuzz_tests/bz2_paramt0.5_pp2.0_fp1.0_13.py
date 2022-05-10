from bz2 import BZ2Decompressor
BZ2Decompressor()

from zlib import decompress
decompress(b'x\x9cK\xca\xc9\xcfK\x06\x00\x1c\x02\x05\x00\x00\x02')

from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\xc0')

from bz2 import BZ2File
bz = BZ2File('./bzipped')
bz.readline()

from zipfile import ZipFile
zf = ZipFile('./zipped')
zf.read('README.txt')

from zlib import compress
compress(b'witch which has which witches wrist watch')

from gzip import compress, decompress
compress(b
