import socket
socket.if_indextoname(1)

#%%
import socket
socket.if_nameindex()

#%%
import socket
socket.if_nametoindex('lo')

#%%
import socket
socket.getaddrinfo('www.google.com', 'http')

#%%
import socket
socket.getaddrinfo('www.google.com', 'http', proto=socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('www.google.com', 'http', 0, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.google.com', 'http', 0, socket.SOCK_STREAM, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.google.com', 'http', 0, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
