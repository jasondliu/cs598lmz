from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz_data)

# %%
from bz2 import BZ2File
file_bz2 = BZ2File('./data/sample.bz2')
file_bz2.read(100)

# %%
file_bz2.seek(0)
file_bz2.read(100)

# %%
file_bz2.seek(0)
file_bz2.read()

# %%
file_bz2.readlines()

# %%
file_bz2.seek(0)
list(file_bz2)

# %%
file_bz2.seek(0)
for line in file_bz2:
    print(line)

# %%
file_bz2.close()

# %%
import gzip
data_gz = open('./data/sample.gz', 'rb').read()
data_gz

# %%
gzip.decompress(data_gz)

# %%
from gzip import open as gzip_open
file_gz
