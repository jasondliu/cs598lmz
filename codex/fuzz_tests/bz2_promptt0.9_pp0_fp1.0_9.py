import bz2
# Test BZ2Decompressor
try:
    bz2.BZ2Decompressor(b'x')
except TypeError:
    hasBZ2 = False
else:
    hasBZ2 = True
# Test LZMADecompressor
try:
    import lzma
except:
    hasLZMA = False
else:
    # See https://bugs.python.org/issue6692
    if sys.version_info[0] < 3 and sys.version_info[1] < 2:
        hasLZMA = False
    else:
        try:
            lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
        except Exception:
            hasLZMA = False
        else:
            hasLZMA = True
FILEMODE_READ = 'rb'
FILEMODE_WRITE = 'wb'
FILEMODE_APPEND = 'ab'
CHUNK_LIMIT = 1024 * 1024
ZLIB = 1
GZIP = 2
BZ2 = 3
LZMA = 4

def open(filename, mode=
