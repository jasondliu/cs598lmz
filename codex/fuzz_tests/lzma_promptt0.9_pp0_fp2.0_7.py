import lzma
# Test LZMADecompressor(format=FORMAT_XZ, memlimit=<memory limit>)
VERSION = 6
OPTION = 2
BLOCK_HEADER = 0xA0
BACK_BLOCK_HEADER = 0xA1
BACK_BLOCK_FOOTER = 0xA2
FILTER_PROPERTIES = 0xA3
INDEX_INDICATOR = 0xA4
INDEX_EMPTY = 0xA5
INDEX_FLAG_PRESENT = 1
INDEX_COUNT_BITS = 24

SIZE_VALID = 0x40
SIZE_UNKNOWN = 0x20

HEADER_MAGIC = b'\xFD7zXZ\x00'

MAGIC_NO_CHECK = b'%n!<vQ-\xd3\xbb+\x0c'
MAGIC_HAS_CHECK = b'\xd3\xbb+\x0c%n!<vQ-'

HEAD_CRC_SIZE = 4

DIC_SIZE_BITS = 23
END_MARK = 0

PADDING = 96


