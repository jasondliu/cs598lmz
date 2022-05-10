from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#%%
import lzma
with lzma.open('C:\\Users\\HP\\Desktop\\test.xz') as f:
    file_content = f.read()

#%%
import gzip
import shutil
with gzip.open('C:\\Users\\HP\\Desktop\\test.gz', 'rb') as f_in:
    with open('C:\\Users\\HP\\Desktop\\test.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

#%%
import bz2
bz2.decompress(data)

#%%
import bz2
with bz2.open('C:\\Users\\HP\\Desktop\\test.bz2', 'rb') as f:
    file_content = f.read()

#%%
import zipfile
zf = zipfile.ZipFile('C:\\Users\\HP\\Desktop\\test.zip')
fp = zf.open('test.txt')
file_content = fp.read()

