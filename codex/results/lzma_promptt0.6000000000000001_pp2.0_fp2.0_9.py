import lzma
# Test LZMADecompressor.__init__()

import lzma

# Initialize with wrong keyword argument
try:
    lzma.LZMADecompressor(bogus=True)
except TypeError:
    pass
else:
    raise RuntimeError("Failed to raise exception for keyword argument")

# Initialize with wrong keyword argument type
try:
    lzma.LZMADecompressor(memlimit="bogus")
except TypeError:
    pass
else:
    raise RuntimeError("Failed to raise exception for keyword argument")

# Initialize with negative memlimit
try:
    lzma.LZMADecompressor(memlimit=-1)
except ValueError:
    pass
else:
    raise RuntimeError("Failed to raise exception for keyword argument")

decompressor = lzma.LZMADecompressor()
decompressor.decompress(b"")

# Test LZMADecompressor.decompress()

import lzma

# Initialize with wrong keyword argument
try:
    lzma.
