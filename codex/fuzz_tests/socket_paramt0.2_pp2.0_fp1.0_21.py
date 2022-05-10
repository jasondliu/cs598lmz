import socket
socket.if_indextoname(3)

# In[ ]:


#if_nameindex()
#This function returns a list of tuples containing the interface index and interface name for all interfaces.
socket.if_nameindex()

# In[ ]:


#if_nametoindex()
#This function returns the interface index for the interface name passed as argument.
socket.if_nametoindex('lo')

# In[ ]:


#gethostbyname()
#This function returns the IP address of the hostname passed as argument.
socket.gethostbyname('www.google.com')

# In[ ]:


#gethostbyname_ex()
#This function returns a tuple containing the hostname, aliaslist, and IP address of the hostname passed as argument.
socket.gethostbyname_ex('www.google.com')

# In[ ]:


#gethostname()
#This function returns the hostname of the machine on which the Python interpreter is running.
socket.gethostname()

# In[ ]:


#gethostbyaddr()
#This function returns a tuple
