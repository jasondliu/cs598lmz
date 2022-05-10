from lzma import LZMADecompressor
LZMADecompressor.decompress(b'')

from lzma import LZMAFile
LZMAFile(open('README.lzma', 'rb'))

from lzma import LZMAError
LZMAError()

from lzma import FILTER_DELTA
from lzma import FILTER_LZMA1
from lzma import FILTER_LZMA2
from lzma import FORMAT_AUTO
from lzma import FORMAT_RAW
from lzma import FORMAT_XZ
from lzma import PRESET_EXTREME
from lzma import PRESET_DEFAULT
from lzma import MODE_FAST
from lzma import MODE_NORMAL
from lzma import CHECK_NONE
from lzma import CHECK_CRC32
from lzma import CHECK_CRC64
from lzma import CHECK_SHA256
