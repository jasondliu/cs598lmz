import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))

# In[ ]:

socket.gethostbyaddr('127.0.0.1')


# In[ ]:

socket.gethostname()


# In[ ]:

socket.gethostbyname('localhost')


# In[ ]:

socket.gethostbyname('www.google.com')

# In[ ]:

socket.getaddrinfo('www.google.com', 80)


# In[ ]:

socket.getaddrinfo('192.168.1.100', 8080)


# In[ ]:

socket.getaddrinfo('192.168.1.100', 8080, socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)


# In[ ]:

socket.getaddrinfo('192.168.1.100', 8080, socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)


# In[ ]:

