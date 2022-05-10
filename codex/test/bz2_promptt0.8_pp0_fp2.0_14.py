import bz2
# Test BZ2Decompressor() and BZ2Compressor() before passing as argument to
# CompressedFile
try:
    bz2.BZ2Decompressor().decompress(b"")
    bz2.BZ2Compressor().compress(b"")
except Exception:
    bz2 = None

