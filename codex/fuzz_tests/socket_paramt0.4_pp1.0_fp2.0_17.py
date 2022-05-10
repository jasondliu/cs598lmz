import socket
socket.if_indextoname(2)

# In[ ]:


# Find the name of the interface on which a given IP address is configured
socket.if_nameindex()

# In[ ]:


# Convert a 32-bit packed IPv4 address (a string four characters in length) to its standard dotted-quad string representation (for example, ‘123.45.67.89’).
socket.inet_ntoa(b'\x7f\x00\x00\x01')

# In[ ]:


# Convert an IP address from its dotted-quad string representation (for example, ‘123.45.67.89’) to the 32-bit packed binary format used in low-level network functions (a string four characters in length).
socket.inet_aton('127.0.0.1')

# In[ ]:


# Convert an IP address from its dotted-quad string representation to its 32-bit packed binary format, and return the binary address in network byte order.
socket.inet_pton(socket.AF_INET, '127.0.0.1')

# In[ ]:


