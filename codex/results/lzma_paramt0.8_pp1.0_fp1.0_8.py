from lzma import LZMADecompressor
LZMADecompressor().decompress(b'XZ\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# $ python3.7 -m lzma -c test.py
# XZ�7zXZ������!�~\�~\}�؛�R�ա�p�\�f+�Ю���*2�h��TO�3�9��W�bv�P�\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\
# �~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�~\�
