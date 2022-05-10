import bz2
bz2_file = bz2.BZ2File('data/example.bz2')
data = bz2_file.read()
bz2_file.close()

data

# In[ ]:


import gzip
gz_file = gzip.open('data/example.gz', 'rt')
data = gz_file.read()
gz_file.close()

data

# In[ ]:


import lzma
xz_file = lzma.open('data/example.xz', 'rt')
data = xz_file.read()
xz_file.close()

data

# #### 7.2.2 压缩数据

# In[ ]:


import bz2
uncompressed_data = b'\n'.join([b'line %d' % i for i in range(1000)])
len(uncompressed_data)

# In[ ]:


bz2_data = bz2.compress(uncompressed_data)
len(bz
