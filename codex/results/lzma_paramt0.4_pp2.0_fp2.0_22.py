from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用bz2模块压缩数据
import bz2
bz2.compress(data)

# 使用bz2模块解压缩数据
import bz2
bz2.decompress(data)

# 使用zlib模块压缩数据
import zlib
zlib.compress(data)

# 使用zlib模块解压缩数据
import zlib
zlib.decompress(data)

# 使用gzip模块压缩数据
import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write(data)

# 使用gzip模块解压缩数
