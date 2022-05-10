import socket
socket.if_indextoname(2)

# In[ ]:


# 使用网络接口的索引获取网络接口的名称
import socket
socket.if_indextoname(3)

# In[ ]:


# 使用网络接口的名称获取网络接口的索引
import socket
socket.if_nametoindex('lo')

# In[ ]:


# 使用网络接口的名称获取网络接口的索引
import socket
socket.if_nametoindex('eth0')

# In[ ]:


# 获取网络接口的信息
import socket
socket.if_nameindex()

# In[ ]:
