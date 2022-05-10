from bz2 import BZ2Decompressor
BZ2Decompressor()

from zlib import decompress
decompress(compressed)

import gzip
import shutil
with gzip.open('/home/user/file.txt.gz', 'rb') as f_in:
    with open('/home/user/file.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# 压缩
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = gzip.compress(s)
len(t)

# 解压缩
import gzip
gzip.decompress(t)

# 将压缩后的数据写入文件
import gzip
with gzip.open('/home/user/file.txt.gz', 'wt') as f:
    f.write(text)
with gzip.open('/home/user/file.txt.gz', 'rt') as f:
    text = f.read
