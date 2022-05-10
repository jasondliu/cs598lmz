import bz2
# Test BZ2Decompressor
# In[ ]:


decompressor = bz2.BZ2Decompressor()
orig_data = []
with open(path_to_bz2_file, 'rb') as f:
    for data in iter(lambda : f.read(100 * 1024), b''):
        data = decompressor.decompress(data)
        if data:
            orig_data.append(data)

print(len(b''.join(orig_data)))
# In[ ]:


# bz2.BZ2Decompressor.decompress seems faster
decompressor = bz2.BZ2Decompressor()
orig_data = []
with open(path_to_bz2_file, 'rb') as f:
    for data in iter(lambda : f.read(100 * 1024), b''):
        data = decompressor.decompress(data)
        if data:
            orig_data.append(data)


orig_data = b''.join(orig_data)
print(len(orig_data))
# In[ ]:


