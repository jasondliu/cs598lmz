from lzma import LZMADecompressor
LZMADecompressor.flush = lambda x: bytes()

# We don't care about the results of the decompression, only that we don't crash.
data = open(sys.argv[1], "rb").read()
assert len(data) == 8

# The flags are the last byte
flags = data[-1]

# The dictionary size is the first four bytes, little-endian
dict_size = struct.unpack('<I', data[:4])[0]

# The lc/lp/pb are the next three bytes
lc, lp, pb = data[4:7]

# First, try decompressing with a preset dictionary
comp = LZMADecompressor(format=FORMAT_AUTO, filters=[
    {"id": FILTER_LZMA1, "dict_size": dict_size},
], preset_dict=b'\x00' * dict_size, lc=lc, lp=lp, pb=pb)
comp.decompress(data[:-1])

# Next, try decompressing with no preset dictionary
comp = LZM
