from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_RAW).decompress(data)

from lzma import open
read = lambda: open(filename, mode="rb").read()
read()

from lzma import open
read = lambda: open(filename, mode="r").read()
read()

from lzma import open
read = lambda: open(filename, mode="rt").read()
read()

from lzma import open
read = lambda: open(filename, mode="rt", encoding="utf-8").read()
read()

from lzma import open
read = lambda: open(filename, mode="rt", encoding="utf-8-sig").read()
read()

from lzma import open
read = lambda: open(filename, mode="rb").read(limit)
read()

from lzma import open
read = lambda: open(filename, mode="r").read(limit)
read()

from lzma import open
read = lambda: open(filename, mode="rt", encoding="utf-8").read(limit)
read()

from lzma import
