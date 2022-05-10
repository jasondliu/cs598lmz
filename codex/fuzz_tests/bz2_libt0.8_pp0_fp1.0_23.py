import bz2
bz2.decompress(compressed_data)

compressed_data = bz2.compress(original_data)
len(compressed_data)

f = open('compress.bz2','wb')
f.write(compressed_data)

f = open('compress.bz2','rb')
f.seek(0)
data = f.read()
original_data = bz2.decompress(data)
len(data)
#%%
import bz2
f = bz2.BZ2File('compress.bz2','wb')
f.write(original_data)
f.close()

f = bz2.BZ2File('compress.bz2','rb')
original_data = f.read()
print(original_data)
len(original_data)
#%%
# lzmai
import lzma

original_data = b'This is the original text.'
with lzma.open('compress.xz', 'wt') as f:
    f.write(original_data
