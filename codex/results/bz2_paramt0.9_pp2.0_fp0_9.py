from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(msg).split('\n')
len(msg)
sum(map(int, BZ2Decompressor().decompress(msg).split('\n')))

# In[14]:

#%%time
import pyximport
pyximport.install(setup_args={"include_dirs": np.get_include()})
import numpy_compress5 as nb
msg = ''.join(line for line in open(_compressed_data, 'r'))
msg = BZ2Decompressor().decompress(msg)
msg = nb.bz_decompress(msg)
msg.split('\n')[200:]
import zlib
x = zlib.decompress(zlib.compress('1223334444'))
x


# In[14]:

x = zlib.compress('1223334444')
x
zlib.compress(x)
nb.bz_decompress('BZh91AY&SY\xd0g\xb1\x02\x01\x01\
