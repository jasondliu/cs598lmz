import socket
socket.if_indextoname(1)

# In[ ]:


#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))

print(s.getsockname()[0])

s.close()


# In[ ]:


#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))

print(s.getsockname()[0])

s.close()


# In[ ]:


#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(("8.8.8.8", 80))

print(s.getsockname()[0])

s.close()


# In[ ]:


#!/usr/
