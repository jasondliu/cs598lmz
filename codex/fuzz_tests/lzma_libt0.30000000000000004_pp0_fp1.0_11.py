import lzma
lzma.decompress(open('/tmp/test.xz', 'rb').read())

# lzma.LZMADecompressor()
# lzma.LZMACompressor()

# lzma.LZMAFile()
# lzma.open()

# lzma.compress()
# lzma.decompress()

# lzma.is_check_supported()
# lzma.CHECK_NONE
# lzma.CHECK_CRC32
# lzma.CHECK_CRC64
# lzma.CHECK_SHA256

# lzma.FORMAT_AUTO
# lzma.FORMAT_XZ
# lzma.FORMAT_ALONE
# lzma.FORMAT_RAW

# lzma.FILTER_LZMA1
# lzma.FILTER_LZMA2
# lzma.FILTER_DELTA
# lzma.FILTER_X86
# lzma.FILTER_IA64
# lzma.FIL
