import bz2
bz2.decompress(compressed)

# In[ ]:


import bz2
for line in bz2.BZ2File('example.bz2'):
    print(line)


# In[ ]:


import bz2
uncompressed = b''
compressed = bz2.compress(uncompressed)
len(uncompressed)
len(compressed)


# In[ ]:


import bz2
uncompressed = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
len(uncompressed)
compressed = bz2.compress(uncompressed)
len(compressed)


# In[ ]:


import bz2
bz2.decompress(compressed)


# In[ ]:


