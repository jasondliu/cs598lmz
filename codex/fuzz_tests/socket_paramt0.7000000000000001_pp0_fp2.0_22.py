import socket
socket.if_indextoname(2)

# In[ ]:


socket.if_indextoname(1)

# In[ ]:


socket.if_indextoname(0)

# In[ ]:


socket.if_indextoname(3)

# In[ ]:


import struct
struct.unpack('=i',b'\x00\x00\x00\x00')

# In[ ]:


struct.unpack('=i',b'\x00\x00\x00\x0A')

# In[ ]:


struct.unpack('=i',b'\x00\x00\x00\xFF')

# In[ ]:


struct.unpack('=i',b'\xFF\xFF\xFF\xFF')

# In[ ]:


struct.unpack('=h',b'\x00\x0A')

# In[ ]:


struct.unpack('=h',b'\xFF\xFF')

# In[ ]:


