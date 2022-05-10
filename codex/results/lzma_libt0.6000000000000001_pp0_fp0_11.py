import lzma
lzma.decompress(encoded_data)

#%%
# 解压缩
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'rb') as f:
    data = f.read()

#%%
# 压缩文件
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'rb') as f:
    data = f.read()

#%%
# 压缩数据
import lzma
data = b'Contents of the example file go here.\n'
