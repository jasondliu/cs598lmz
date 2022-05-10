import bz2
bz2.decompress(data)

# In[ ]:


# 将数据压缩后写入文件
with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(data)

# In[ ]:


# 读取压缩文件
with bz2.BZ2File('spam.bz2', 'rb') as f:
    file_content = f.read()

# In[ ]:


file_content

# In[ ]:


# 压缩文件的压缩率
len(data), len(file_content)

# In[ ]:


# 压缩率
len(data) / len(file_content)

# ## 压缩文件的读取

# In[ ]:


import bz2
import os

# In[ ]:


#
