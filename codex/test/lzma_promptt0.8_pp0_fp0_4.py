import lzma
# Test LZMADecompressor.
# The decompressor has to be fed one byte at a time, to check it
# doesn't read more than that.  We do this by wrapping in a
# StringIO and calling read(1).
import io

