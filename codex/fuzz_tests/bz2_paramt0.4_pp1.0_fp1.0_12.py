from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# Compression and decompression with zlib
import zlib
s = b'witch which has which witches wrist watch'
len(s)

# In[ ]:


t = zlib.compress(s)
len(t)

# In[ ]:


zlib.decompress(t)

# In[ ]:


zlib.crc32(s)

# In[ ]:


# Base64 encoding and decoding
import base64
s = b'hello'
a = base64.b64encode(s)
a

# In[ ]:


base64.b64decode(a)

# In[ ]:


# Base64 encoding and decoding as a MIME attachment
s = b'hello'
a = base64.b64encode(s)
a

# In[ ]:


a.decode('ascii')

# In[ ]:


from email.mime.text import MIMEText
m = MIMEText(
