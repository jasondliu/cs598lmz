from lzma import LZMADecompressor
LZMADecompressor.__module__

# %%
path = "wsj_0010_sample.tar.bz2"
import bz2
with bz2.open(path, 'rb') as f:
    data = f.read()
data[:10]

# %%
path = "wsj_0010_sample.tar.xz"
with lzma.open(path, 'rb') as f:
    file_content = f.read()
file_content[:10]

# %%
path = "wsj_0010_sample.tar.bz2"
data = bz2.decompress(path)
data[:10]

# %%
path = "wsj_0010_sample.tar.xz"
data = lzma.decompress(path)
data[:10]

# %%
bzip2.compress(data)

# %%
lzma.compress(data)

# %%
path = 'wsj_0010_sample.txt'
import os
os.path.getsize(path)

# %%

