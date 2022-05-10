import lzma
lzma.LZMA_VERSION

# In[ ]:


#lzma.LZMACompressor().compress(data)
#lzma.LZMADecompressor().decompress(data)

# In[ ]:


with lzma.open("LICENSE.xz") as f:
    print(f.read())

# In[ ]:


#lzma.is_check_supported(lzma.CHECK_CRC32)
#lzma.is_check_supported(lzma.CHECK_CRC64)
#lzma.is_check_supported(lzma.CHECK_SHA256)

# In[ ]:


#lzma.is_check_supported(lzma.CHECK_NONE)
#lzma.is_check_supported(lzma.CHECK_ID_MAX)

# In[ ]:


#lzma.CHECK_CRC64
#lzma.CHECK_CRC32
#lzma.CHECK_SHA256
#lzma
