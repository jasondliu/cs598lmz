import bz2
bz2.BZ2File(path + 'train-images-idx3-ubyte.bz2', 'r')

#%%
import gzip
with gzip.open(path + 'train-labels-idx1-ubyte.gz', 'rb') as f:
    file_content = f.read()

#%%
type(file_content)

#%%
file_content[0:4]

#%%
import struct

#%%
msb_uint32 = file_content[0:4]
struct.unpack('>I', msb_uint32)

#%%
msb_uint32 = file_content[4:8]
struct.unpack('>I', msb_uint32)

#%%
msb_uint32 = file_content[8:12]
struct.unpack('>I', msb_uint32)

#%%
msb_uint32 = file_content[12:16]
struct.unpack('>I', msb_uint32)

#%%
msb_uint32 =
