import lzma
lzma.open

# We should get the lzma module, even though the lzma module is
# named lzma in Python 3:
import lzma
assert lzma.open == lzma._lzma.open

raise SystemExit(0)
