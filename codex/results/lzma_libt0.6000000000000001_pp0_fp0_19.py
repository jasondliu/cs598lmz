import lzma
lzma.LZMAError

# pylint: disable=unused-import
from . import _lzma as lzma
from .lzma_file import LZMACompressor, LZMADecompressor
from .lzma_file import LZMARandomFile as LZMAFile
from .lzma_file import LZMAError
from .lzma_file import lzma_compresslevel
from .lzma_file import lzma_preset
from .lzma_file import lzma_version
from .lzma_file import lzma_version_info
from .lzma_file import lzma_is_check_supported
from .lzma_file import lzma_check_is_supported
from .lzma_file import lzma_check_size
from .lzma_file import lzma_filter_names
from .lzma_file import lzma_mode
from .lzma_file import lzma_mtime
from .lzma_file import lzma
