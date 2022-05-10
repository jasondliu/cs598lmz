from lzma import LZMADecompressor
LZMADecompressor().decompress(open("data/dictionary.txt.xz", "rb").read())

# 10.2.2.2. LZMA compression
from lzma import LZMACompressor
comp = LZMACompressor()
comp.compress(b"some data")
comp.compress(b"some more data")
comp.flush()

# 10.2.2.3. BZIP2 compression and decompression
import bz2
bz2.decompress(open("data/dictionary.txt.bz2", "rb").read())

# 10.2.2.4. BZIP2 compression
import bz2
comp = bz2.BZ2Compressor()
comp.compress(b"some data")
comp.compress(b"some more data")
comp.flush()

# 10.2.2.5. ZLIB compression and decompression
import zlib
zlib.decompress(open("data/dictionary.txt.zlib", "rb").read())

# 10.2.2.6. Z
