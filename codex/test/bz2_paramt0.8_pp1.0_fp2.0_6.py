from bz2 import BZ2Decompressor
BZ2Decompressor()

# Py2: ImportError: No module named bz2
# Py3: TypeError: start_bz2decompressor() missing 1 required positional argument: 'wbits'
