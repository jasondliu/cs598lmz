import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
dec_data = bz2_decompressor.decompress(comp_data)
dec_data

# In[18]:


# import bz2
# Test BZ2File
with bz2.BZ2File('test.bz2', 'wb') as f:
    f.write(data)
with bz2.BZ2File('test.bz2', 'rb') as f:
    f.read()
# bz2.open('test.bz2')


# In[19]:


# import lzma
# Test LZMACompressor
lzma_compressor = lzma.LZMACompressor()
comp_data = lzma_compressor.compress(b'Hello World, ' * 100)
comp_data

# In[20]:


# import lzma
# Test LZMADecompressor
lzma_decompressor = lzma.LZMADecompressor()
dec_
