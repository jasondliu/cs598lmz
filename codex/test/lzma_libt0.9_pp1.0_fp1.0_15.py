import lzma
lzma.open('test.lzma')

try:
    import bz2
    bz2.BZ2Compressor()
except ImportError:
    bz2 = None

