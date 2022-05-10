from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# get_ipython().run_cell_magic('time', '', '\n# Decompress using BZ2Decompressor\n\ndecompressor = BZ2Decompressor()\ndata = bz2_data\nresult = b\'\'\nwhile True:\n    chunk = decompressor.decompress(data)\n    if chunk == b\'\':\n        break\n    result += chunk\n    data = data[len(data)//2:]\n    \nprint(len(result))')

# In[ ]:


# get_ipython().run_cell_magic('time', '', '\n# Decompress using bz2.decompress\n\nresult = bz2.decompress(bz2_data)\nprint(len(result))')

# In[ ]:


# get_ipython().run_cell_magic('time', '', '\n# Decompress using bz2.decompress\n\nresult = bz
