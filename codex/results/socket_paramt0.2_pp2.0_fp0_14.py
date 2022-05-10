import socket
socket.if_indextoname(3)

#%%
import socket
socket.if_nametoindex('lo')

#%%
import socket
socket.gethostbyname('localhost')

#%%
import socket
socket.gethostbyname_ex('localhost')

#%%
import socket
socket.gethostbyaddr('127.0.0.1')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.getfqdn('localhost')

#%%
import socket
socket.getaddrinfo('localhost', 80)

#%%
import socket
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

#%%
import socket
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE, socket.IPPROTO_TCP)

