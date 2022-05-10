import socket
socket.if_indextoname(2)

# This returns the name of the interface from the index
# provided.


# In[ ]:


# Create a socket object

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# In[ ]:


# Get local machine name

host = socket.gethostname()


# In[ ]:


host


# In[ ]:


port = 9999


# In[ ]:


# Connection to hostname on the port.

s.connect((host, port))


# In[ ]:


# Receive no more than 1024 bytes

tm = s.recv(1024)


# In[ ]:


s.close()


# In[ ]:


print("The time got from the server is %s" % tm.decode('ascii'))
