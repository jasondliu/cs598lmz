from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("train.ft.txt.bz2").read())

# In[ ]:


import bz2
file = bz2.BZ2File("train.ft.txt.bz2")
file.readline()

# ## Unzipping the training file

# In[ ]:


import bz2
un = bz2.BZ2File("train.ft.txt.bz2")
file_content = un.readlines()

# In[ ]:


len(file_content)

# ## Reading the training file

# In[ ]:


import bz2
un = bz2.BZ2File("train.ft.txt.bz2")
file_content = un.readlines()

# In[ ]:


len(file_content)

# In[ ]:


file_content[0]

# In[ ]:


file_content[0].decode('utf-8')

# In[ ]:


file_content[0].decode('utf-8
