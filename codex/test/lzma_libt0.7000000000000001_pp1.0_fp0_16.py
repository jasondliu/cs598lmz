import lzma
lzma.open

# This is a hack. We know how to decompress the data, but we don't have a
# file-like object that supports seek(), so we have to load the whole thing
# into memory.
