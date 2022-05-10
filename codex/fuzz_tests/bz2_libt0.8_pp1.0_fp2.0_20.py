import bz2
bz2.decompress(data)

# In[41]:

import gzip
f = gzip.open('file.txt.gz', 'rb')
file_content = f.read()


# In[43]:


import zipfile
z = zipfile.ZipFile('file.zip','r')
z.extractall('dir')
