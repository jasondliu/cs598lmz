from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

from gzip import GzipFile
GzipFile(mode='rb', fileobj=io.BytesIO(data)).read()

from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

from zlib import decompress
decompress(data)
</code>
You can read more about compression and decompression in the official Python documentation.

