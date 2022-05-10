from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#(b'Hello World!', b'')

from bz2 import decompress
decompress(data)

#b'Hello World!'

from zlib import decompress
decompress(data)

#b'Hello World!'
</code>

