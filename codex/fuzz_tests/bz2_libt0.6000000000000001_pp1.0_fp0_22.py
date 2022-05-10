import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 小文件压缩

import gzip
with gzip.open('../testfile/test.txt.gz', 'wt') as f:
    f.write('hello gzip')

with gzip.open('../testfile/test.txt.gz', 'rt') as f:
    print(f.read())

import bz2
with bz2.open('../testfile/test.txt.bz2', 'wt') as f:
    f.write('hello bz2')

with bz2.open('../testfile/test.txt.bz2', 'rt') as f:
    print(f.read())

# 大文件压缩

import gzip
with gzip.open('../testfile/test.txt.gz', 'rb') as f_in:
    with open('../testfile/test.txt', 'wb') as f_out:
        shutil.copyfileobj(
