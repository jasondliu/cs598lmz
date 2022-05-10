import bz2
# Test BZ2Decompressor class
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# bz2.BZ2Compressor.__init__(compresslevel=9, flush=0,
#                            randfunc=None, wbits=15)
compressor = bz2.BZ2Compressor(wbits=16 + 9)
compressor.compress(data)
compressor.flush()

# bz2.compress(data, compresslevel=9)
bz2.compress(data)

# bz2.decompress(data)
bz2.decompress(compressed_data)

# bz2.open(filename, mode="r", compresslevel=9,
#          encoding=None, errors=None, newline=None)
bz2_file = bz2.open("/tmp/bz2_file.bz2", mode="wt", compresslevel=9)
bz2_file.write("content\n")
bz2_file.write("content
