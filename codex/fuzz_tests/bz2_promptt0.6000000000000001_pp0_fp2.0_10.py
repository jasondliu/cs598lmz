import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()
data = d.decompress(b_data)
data

# Test BZ2Compressor

c = bz2.BZ2Compressor()
c.compress(b_data)
c.flush()
 
# Test BZ2File

bz2.BZ2File('./data/compressed.bz2')
bzip_file = bz2.BZ2File('./data/compressed.bz2', mode='w')
bzip_file.write(b_data)
bzip_file.close()
 
bz2.BZ2File('./data/compressed.bz2')
 
bzip_file = bz2.BZ2File('./data/compressed.bz2')
bzip_file.read(100)
bzip_file.tell()
bzip_file.seek(0)
bzip_file.read()
bzip_file.seek(0)
bzip_file.readlines()

