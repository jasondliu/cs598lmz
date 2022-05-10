import socket
socket.if_indextoname('1')

# In[41]:


socket.if_nametoindex('lo')

# In[39]:


import socket
socket.if_indextoname(2)


# In[ ]:


import socket
socket.if_indextoname(3)


# In[ ]:


import socket
socket.if_nametoindex('enp2s0')


# In[ ]:


#10.7.1.1
#10.7.1.2


# In[ ]:


import ipaddress
ipaddress.ip_address('10.7.1.1')


# In[ ]:


import ipaddress
ipaddress.ip_address('10.7.1.1/24')


# In[ ]:


import ipaddress
ipaddress.ip_address('10.7.1.1/24').reverse_pointer


# In[ ]:


import ipaddress
ipaddress.ip_address('10.7.1.1/24')


# In[ ]:


import ipaddress
ipaddress
