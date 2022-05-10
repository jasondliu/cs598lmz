from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x5d\x00\x00\x80\x00')

# ======================================================================= #
#                                LZ4                                      #
# ======================================================================= #
# Compress with lz4
from lz4 import frame
frame.compress(b'Hello World', mode='fast')

# Decompress with lz4
from lz4 import frame
frame.decompress(b'\x02\x21\x4c\x18"\x00\x11HKME-LZ4\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x0c\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00HELLO WORLD')

# ======================================================================= #
#                                BZ2
