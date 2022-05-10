import socket
socket.if_indextoname(3)

#%%
import socket
socket.if_nameindex()

#%%
import socket
socket.if_nametoindex('lo')

#%%
import socket
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.google.com', None)

#%%
import socket
socket.getaddrinfo('127.0.0.1', 8080, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)

#%%
import socket
socket.getaddrinfo('127.0.0.1', 8080, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('127.0.0.1', 8080, socket.AF_INET, 0, 0, socket.AI_PASSIVE)

#%%
import socket
socket
