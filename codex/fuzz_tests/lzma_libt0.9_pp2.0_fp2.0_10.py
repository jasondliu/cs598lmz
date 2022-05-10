import lzma
lzma.format_warning("Compression test", lzma.FORMAT_ALONE)
lzma.format_warning("Compression test", lzma.FORMAT_XZ)
lzma.format_warning("Compression test", lzma.FORMAT_RAW)
lzma.MODE_FAST
lzma.check_is_supported(lzma.CHECK_CRC32)
lzma.check_is_supported(lzma.CHECK_CRC64)
lzma.check_is_supported(lzma.CHECK_SHA256)

i = lzma.FILTER_ARM
while i <= lzma.FILTER_LZMA2:
    lzma.filter_is_supported(i)
    i += 1

s = lzma.stream(-1, lzma.CHECK_CRC64, 
                filters=[{"id": lzma.FILTER_LZMA2,
                          "preset": 9 | lzma.PRESET_EXTREME}])
s = lzma.stream(-
