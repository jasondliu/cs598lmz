import bz2
bz2.BZ2File('tempdata/ssa-babynames-nationwide-2014.txt.bz2').readlines()[:10]

# Compression ratios
import os
bz2_size = os.path.getsize('tempdata/ssa-babynames-nationwide-2014.txt.bz2')
print(bz2_size)
raw_size = os.path.getsize('tempdata/ssa-babynames-nationwide-2014.txt')
print(raw_size)
compression_ratio = bz2_size / raw_size
print(format(compression_ratio, '%'))

# Uncompressing a bzip2 File
import bz2
f_in = bz2.BZ2File('tempdata/ssa-babynames-nationwide-2014.txt.bz2', 'r')
f_out = open('tempdata/uncompressed.txt', 'wb')
f_out.write(f_in.read())
f_out.close()
f_in
