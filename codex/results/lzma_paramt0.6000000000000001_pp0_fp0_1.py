from lzma import LZMADecompressor
LZMADecompressor().decompress(b"")

# LZMAFile
from lzma import LZMAFile
LZMAFile(fileobj=None, mode="r", format=None, check=-1, preset=None, filters=None)

# LZMAError
from lzma import LZMAError
LZMAError()

# open
from lzma import open
open(filename, mode="r", format=None, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)
