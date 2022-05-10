from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# In[3]:


import sys
sys.getsizeof(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# In[4]:


import lzma
with lzma.open('zen.xz', 'rt', encoding='utf-8') as f:
    text = f.read()
text

# In[5]:


import zlib
s = b'witch which has which witches wrist watch'
len(s)

# In[6]:


t = zlib.compress(s)
len(t)

# In[
