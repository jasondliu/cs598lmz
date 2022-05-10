import bz2
bz2.decompress(bz2_data)


# In[18]:


bz2.decompress(bz2_data) == uncompressed_data


# In[19]:


from io import BytesIO
uncompressed = BytesIO(uncompressed_data)
compressed = BytesIO()
compressor = bz2.BZ2Compressor()
while True:
    chunk = uncompressed.read(1024)
    if not chunk:
        break
    compressed.write(compressor.compress(chunk))
compressed.write(compressor.flush())
compressed.seek(0)
bz2.decompress(compressed.read()) == uncompressed_data


# In[20]:


import zlib
compressor = zlib.compressobj(1)
compressed_data = compressor.compress(uncompressed_data)
compressed_data += compressor.flush()
len(compressed_data)


# In[21]:


decompressor = zlib.decompressobj()
decompressed_data
