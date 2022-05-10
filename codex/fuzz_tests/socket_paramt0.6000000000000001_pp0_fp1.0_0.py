import socket
socket.if_indextoname(1)

# In[ ]:


#!/usr/bin/python

import socket
socket.if_nameindex()

# In[ ]:


#!/usr/bin/python

import socket
socket.getaddrinfo("www.google.com", 80, 0, 0, socket.IPPROTO_TCP)
