import socket
socket.if_indextoname(3)

# In[ ]:


# 可以用socket.if_nameindex()来获取所有接口的名字和索引
socket.if_nameindex()

# In[ ]:


# 获取本机的IP地址
socket.gethostbyname(socket.gethostname())

# In[ ]:


# 获取本机的IP地址
socket.gethostbyname_ex(socket.gethostname())

# In[ ]:


# 获取本机的MAC地址
def get_host_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

# In[ ]:


get_host_mac_address()

# In[
