import bz2
bz2.decompress(data)

# bz2.open(filename [, mode [, compresslevel]])
# bz2.BZ2File(filename [, mode [, compresslevel]])
import bz2
bz2_file_obj = bz2.BZ2File('file.bz2')
data = bz2_file_obj.read()
bz2_file_obj.close()

# bz2.compress(data [, compresslevel])
# bz2.BZ2Compressor([compresslevel])
import bz2
bz2_compressor = bz2.BZ2Compressor()
bz2_compressor.compress(b"some data")
bz2_compressor.flush()
# 如果没有调用flush结果会不完整

import gzip
with gzip.open('file.gz', 'wt') as f:
    f.write(data)

# gzip.open(filename, mode='
