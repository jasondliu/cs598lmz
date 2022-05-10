import socket
socket.if_indextoname(2)

#%%
import socket
socket.if_nametoindex('lo')

#%%
import socket
socket.gethostbyname('localhost')

#%%
import socket
socket.gethostbyaddr('127.0.0.1')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.getfqdn('127.0.0.1')

#%%
import socket
socket.getfqdn()

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME)

#%%
import socket
socket.getaddrinfo('www.python.
