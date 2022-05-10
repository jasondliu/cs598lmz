from lzma import LZMADecompressor
LZMADecompressor32 = partial(LZMADecompressor, format=LZMA_FORMAT_X86, threads=1)
LZMADecompressor64 = partial(LZMADecompressor, format=LZMA_FORMAT_X86_BCJ2)

from warnings import warn

from .compression import CompressedFile, CompressedStream
from .util import (
	Archive, ArchiveEntry, ArchiveInterface,
	decode_string, iterator_expect,
	LITTLE_ENDIAN, MEDIUM_ENDIAN, BIG_ENDIAN
)

from ..exceptions import (
	NotAnMWArchiveError, CorruptArchiveError,
	ExpectedMoreDataError, ArchiveVersionError,
	FormatNotSupportedError
)


__all__ = [
	# Constants
	'TES4_MAGIC', 'TES4_HEADER_SIZE', 'TES4_HEADER_SIZE_MIN',
	'TES4_RECORD_TYPES',
	# Classes
	'TES4Record', 'TES4', 'SENIL
