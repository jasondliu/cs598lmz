import lzma
lzma.LZMADecompressor


# Try bz2
import bz2
bz2.BZ2Decompressor()


# Try unrar
try:
    import unrar
except ImportError:
    class Unrar(object):
        open = None
        unrar = None

    unrar = Unrar()
