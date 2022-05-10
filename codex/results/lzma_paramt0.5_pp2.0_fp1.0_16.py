from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00')

# The lzma module is not part of the Python Standard Library.
# It is an optional module that can be installed using pip.
# $ python3 -m pip install lzma
#
# To compress data using LZMA, you need to create an LZMACompressor
# object and feed it data using its compress() method.
# To decompress data, you need to create an LZMADecompressor object
# and feed it the compressed data using its decompress() method.
