import bz2
# Test BZ2Decompressor
bz = bz2.BZ2Decompressor()
bz.decompress(bz2.decompress(bz2_data))

# Test BZ2File
bzf = bz2.BZ2File(io.BytesIO(bz2.decompress(bz2_data)))
bzf.read()

# Test BZ2File, compression
bzf = bz2.BZ2File(io.BytesIO(), 'w')
bzf.write(bz2.decompress(bz2_data))
bzf.close()

# Test BZ2File, decompression
bzf = bz2.BZ2File(io.BytesIO(bz2.decompress(bz2_data)))
bzf.read()
bzf.close()
