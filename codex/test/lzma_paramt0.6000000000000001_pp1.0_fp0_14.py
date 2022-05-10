from lzma import LZMADecompressor
LZMADecompressor()

try:
    from lzma import LZMACompressor
    LZMACompressor()
except ImportError:
    pass

try:
    from lzma import open
    open(__file__, mode="rt", encoding="utf-8")
except ImportError:
    pass

# Issue #11098
import lzma
lzma.open(__file__)

# Issue #12790
import lzma
lzma.open(__file__, "rt", encoding="utf-8")

# Issue #12848
import lzma
lzma.LZMAFile(__file__)

# Issue #12848
import lzma
lzma.LZMAFile(__file__, "r")

# Issue #12848
import lzma
