import bz2
# Test BZ2Decompressor

crc = zlib.crc32

data = open(testmod.__file__, "rb").read()
data = data + (b"x" * 1000000)
compobj = bz2.BZ2Compressor()

# Compress the data
co = compobj.compress(data)
co = co + compobj.flush()
del data

# Decompress the compressed data
decompobj = bz2.BZ2Decompressor()
decompobj.decompress(co)  # Issue #17188
# decompobj.decompress(co)  # Issue #17188
# decompobj.decompress(b"x" * 100)

# Try to decompress more data than there is in the compressed stream
with test_support.check_py3k_warnings():
    try:
        decompobj.decompress(b"x" * 100)
    except EOFError:
        pass

# Create a large compressed stream
with open("largefile.bz2.out", "wb") as out:
    compobj =
