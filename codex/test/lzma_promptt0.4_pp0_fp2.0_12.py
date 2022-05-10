import lzma
# Test LZMADecompressor

import lzma
from io import BytesIO
from lzma import LZMADecompressor
from lzma import LZMAFile
from lzma import LZMAError
from lzma import FORMAT_AUTO
from lzma import FORMAT_XZ
from lzma import CHECK_CRC32
from lzma import CHECK_CRC64
from lzma import CHECK_SHA256
from lzma import FILTER_LZMA1
from lzma import FILTER_LZMA2
from lzma import MODE_FAST
from lzma import MODE_NORMAL
