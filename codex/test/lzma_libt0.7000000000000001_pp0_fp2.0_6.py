import lzma
lzma.decompress(lzma.compress(b'a' * 100000))

del lzma

# Cannot open lzma.so, so an ImportError is the expected behavior
import lzma

# =====================================================================
# Cleanup
# =====================================================================

