import lzma
# Test LZMADecompressor output when we read the entire source at once.

t = b'this is a test'

e = lzma.compress(t)
s = lzma.LZMADecompressor().decompress(e)

print(s)
compress = lzma.compress
compressobj = lzma.compressobj
decompress = lzma.decompress
decompressobj = lzma.decompressobj
LZMADecompressor = lzma.LZMADecompressor
LZMAError = lzma.LZMAError
FORMAT_AUTO = lzma.FORMAT_AUTO
FORMAT_XZ = lzma.FORMAT_XZ
FORMAT_ALONE = lzma.FORMAT_ALONE
FORMAT_RAW = lzma.FORMAT_RAW
CHECK_NONE = lzma.CHECK_NONE
CHECK_CRC32 = lzma.CHECK_CRC32
CHECK_CRC64 = lzma.CHECK_CRC64
CHECK_SHA256
