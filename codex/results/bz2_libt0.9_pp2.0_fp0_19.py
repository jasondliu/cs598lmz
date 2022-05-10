import bz2
bz2.compress(decompressed) 


# In[5]:


# write to text file


# In[6]:


decompressed = bz2.decompress(bz2.compress(decompressed))
decompressed


# ### Compression Ratio

# In[7]:


s = 'hello, how are you today? you are amazing dude'


# In[8]:


f = gzip.open('data/s.txt', 'wt')
f.write(s)
f.close()


# In[9]:


f = gzip.open('data/s.txt', 'rt')
g = gzip.open('data/s_v2.txt', 'wt')
g.write(f.read())


# In[10]:


f = gzip.open('data/s.txt', 'rt')
original_file = f.read()
original_file


# In[11]:


f = gzip.open('data/s_v2.txt', 'rt')
compressed_file = f.
