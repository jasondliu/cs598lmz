import lzma
lzma.LZMADecompressor.decompress

# lzma.LZMADecompressor.decompress(data, max_length=-1, format=FORMAT_AUTO, memlimit=None, filters=None)
# Return decompressed data as bytes.

# If the format parameter is FORMAT_XZ, the data must be the raw, compressed data, without the .xz file header or footer.

# If the format parameter is FORMAT_ALONE, the data must be the .xz file header followed by the raw, compressed data.

# If the format parameter is FORMAT_RAW, the data must be the .xz file header, the raw, compressed data, and the .xz file footer.

# If the format parameter is FORMAT_AUTO (the default), the decompressor tries to auto-detect the file format by looking at the first few bytes of the data. If the data doesn’t start with the .xz file header, FORMAT_RAW is assumed.

# If the data is compressed with the LZMA1 or LZMA2 filter
