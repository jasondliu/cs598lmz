import bz2
# Test BZ2Decompressor
bzd = bz2.BZ2Decompressor()
bzd.decompress(bz2_data)
bzd.flush()
# Test BZ2File
bzf = bz2.BZ2File(io.BytesIO(bz2_data))
bzf.read()
bzf.close()
# Test BZ2Compressor
bzc = bz2.BZ2Compressor()
bzc.compress(data)
bzc.flush()
# Test BZ2File
bzf = bz2.BZ2File(io.BytesIO(), 'w')
bzf.write(data)
bzf.close()
# Test BZ2File.readline()
bzf = bz2.BZ2File(io.BytesIO(bz2_data))
bzf.readline()
bzf.close()
# Test BZ2File.readlines()
bzf = bz2.BZ2File(io.BytesIO(bz2_data))
