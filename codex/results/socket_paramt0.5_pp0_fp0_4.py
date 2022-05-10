import socket
socket.if_indextoname(3)

# This will return the name of the network interface associated with the index number 3.

# In[6]:


import socket
socket.if_nameindex()

# This will return a list of tuples containing the name and index of all the network interfaces.

# In[7]:


import socket
socket.if_nametoindex('lo')

# This will return the index of the network interface associated with the name 'lo'.

# In[8]:


import socket
socket.getnameinfo(('127.0.0.1', 80), 0)

# This will return a tuple containing the hostname and the service associated with the port 80.

# In[9]:


import socket
socket.getnameinfo(('127.0.0.1', 80), 0)

# This will return a tuple containing the hostname and the service associated with the port 80.

# In[10]:


import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NOFQDN)

# This will return a tuple containing the
