from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# $ python3
# Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
# [GCC 7.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from lzma import LZMADecompressor
# >>> LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')
# b'hello'
# >>>
