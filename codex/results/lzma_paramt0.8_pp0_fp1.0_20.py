from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

'''
from lzma import LZMADecompressor
d=LZMAStreamDecompressor()
d.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')
'''

file = open("data.lzma")
contents = file.read()
file.close()
from lzma import LZMADecompressor
LZMADecompressor().decompress(contents)

from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\
