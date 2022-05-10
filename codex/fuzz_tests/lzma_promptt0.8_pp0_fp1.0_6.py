import lzma
# Test LZMADecompressor for decompressing XZ files

# References:
# http://tukaani.org/xz/xz-file-format.txt

# XZ Header:
# Offset  Length  Description
# 0       6       Signature 6 bytes: {0xFD, '7', 'z', 'X', 'Z', 0x00}
# 6       2       Stream Flags (default: {0x00, 0x00})
# 8       4       Stream Header Size (default: {0x00, 0x00, 0x00, 0x08})
# 12      8       Stream Header CRC32 (default: {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00})
#
# The default Stream Flags and default Stream Header Size values are
# equivalent to the following, in little-endian form:
#
# Offset  Length  Description
# 0       4       Flags
# 4       4       Backward Size
#
# Stream Flags:
# Bit  Name                Description
# 0    version             Stream Version (0 = v1.
