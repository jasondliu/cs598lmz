import lzma
lzma.LZMA_AVAILABLE = False
from lzma import LZMAFile

from . import _lzma
from . import _lzma_decompress

from . import _lzma_encode
from . import _lzma_decode
from . import _lzma_encode_filter
from . import _lzma_decode_filter

from . import _lzma_format
from . import _lzma_filter
from . import _lzma_mode
from . import _lzma_mf
from . import _lzma_check
from . import _lzma_preset
from . import _lzma_ret
from . import _lzma_stream_flags
from . import _lzma_version

from . import _lzma_easy_preset
from . import _lzma_easy_encoder
from . import _lzma_easy_decoder

from . import _lzma_lzma_preset
from . import _lzma_lzma
