from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma)


# In[17]:


lzma1=pd.DataFrame(lzma)
lzma1


# In[18]:


lzma2=lzma1[lzma1[1]=='LZMA']
lzma2


# In[19]:


len(lzma2)


# In[20]:


lzma3 = list(lzma2[0])
lzma3


# In[21]:


lzma3[0]


# In[22]:


json_file=urllib.request.urlopen(lzma3[0])


# In[23]:


lzma4=lzma.compress(json_file.read())
lzma4


# In[24]:


import sys
sys.getsizeof(lzma4)


# In[25]:


import xmltodict
lzma5=xmltodict.parse(lzma4)


# In
