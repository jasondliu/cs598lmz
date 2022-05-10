from lzma import LZMADecompressor
LZMADecompressor.decompress(xz(b'\x00\x00\x00\x00\x01'))

#------------------------------------------------------------------------------#
# The LZMA/XZ Decoder Support Package.                                         #
#------------------------------------------------------------------------------#

# struct_lzma.py
# Because the LZMA format is not in standard Python, we need this file to
# provide the necessary structure format.
# License: Python Software Foundation License

from ctypes import LittleEndianStructure, c_uint32, c_uint16, c_byte, sizeof

# Flags
LZMA_TELL_NO_CHECK       = 0x01
LZMA_TELL_UNSUPPORTED_CHECK = 0x02
LZMA_TELL_ANY_CHECK      = 0x04
LZMA_CONCATENATED        = 0x08

# Integrity check types
LZMA_CHECK_NONE          = 0x00
LZMA_CHECK_CRC32         = 0x01
LZMA_CHECK_CRC64         = 0x04
LZMA_CHECK_SHA256        =
