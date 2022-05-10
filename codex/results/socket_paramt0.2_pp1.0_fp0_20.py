import socket
socket.if_indextoname(1)

# In[ ]:


# 获取本机ip
import socket
socket.gethostbyname(socket.gethostname())

# In[ ]:


# 获取本机mac地址
import uuid
uuid.UUID(int = uuid.getnode()).hex[-12:]

# In[ ]:


# 获取本机mac地址
import uuid
''.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
for ele in range(0,8*6,8)][::-1])

# In[ ]:


# 获取本机mac地址
import uuid
''.join(c + ':' if i % 2 else c for i,c in 
enumerate(hex(uuid.getnode())[2:].zfill(12)))[:-1]

# In[ ]:


# 获取
