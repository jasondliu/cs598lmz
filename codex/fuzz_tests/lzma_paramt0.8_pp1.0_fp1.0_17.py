from lzma import LZMADecompressor
LZMADecompressor().decompress(ciphertext)

# Exercise 2
import binascii
ciphertext = b'5\xeeV\x08\x9e\x9b\xa6\x8c\x81\x93\x93\x18\x8b\xe7\xc1\x9d\xe1\x01\x85\xb0\n.\xf6\xd8\x1d\xed\xf9\xcd\x8e\x1e\x0f\x0e\xda\x9d\xa9\x0e\xcb\xab\xcb\x1d\x1d\x5e\x9e\xd3\xc9\x06\xca\xa7\xcf\xeb\xbd\xbc5\x7f\xcc\x9f\xbf\x03\t\xac\x00\xd0\x1e\xed\xb9\x9e\xfa\x1f\x05\xeb\x01\xb0\x
