import socket
socket.if_indextoname(index)

#%%
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
s.getsockname()[0]

#%%
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
s.getsockname()[0]

#%%
import socket
socket.gethostbyname('localhost')

#%%
import socket
socket.gethostbyaddr('127.0.0.1')

#%%
import socket
socket.getfqdn('127.0.0.1')

#%%
import socket
socket.gethostbyname_ex('localhost')

#%%
import socket
socket.getaddrinfo('localhost', 80)

#%%
import socket
socket.getaddrinfo('localhost', 80, AF_INET)


