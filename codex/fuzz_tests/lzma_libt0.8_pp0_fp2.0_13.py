import lzma
lzma.decompress()
print("*"*30)

#lzma.LZMACompressor(format=None, check=-1, preset=None, filters=None)
#lzma.LZMADecompressor(format=None, memlimit=None, filters=None)

class LZMAcompressor:

    # format = 0    0 = LZMA (default)
    #        = 1    1 = XZ (decompression only)
    #        = 2    2 = raw LZMA (no container, decompression only)
    #
    # check = 0    0 = no integrity checks (default)
    #       = 1    1 = CRC32 integrity check
    #       = 2    2 = CRC64 integrity check
    #       = 3    3 = SHA256 integrity check
    #
    # preset:
    #           0..9: Compression
    #           0 = Fastest compression
    #           1 = Fast compression
    #           6 = Default compression
    #           9 = Best compression
    #           18..24: Decompression-only (raw
