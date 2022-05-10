import bz2
bz2_compressor = bz2.BZ2Compressor()
bz2_compressor.compress(b"This is an example text.")
# b"BZ"
bz2_compressor.flush()
# b"h\x9e=8\xff\xf2I\x06,\x00\x02\xff\xee\xe3\x92MYL!\xe2"

import gzip

data = open('README.md', 'rb').read()
len(data)
# 788

t_start = time()
f_bz2 = bz2.open('README.bz2', 'wb')
f_bz2.write(data)
f_bz2.close()
time() - t_start
# 1.1110332019799854

t_start = time()
f_gzip = gzip.open('README.gz', 'wb')
f_gzip.write(data)
f_gzip.close()
time() - t_start
# 0.701223753093
