import socket
socket.if_indextoname(3)

#%%
import socket
socket.if_nameindex()

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_CANONNAME, socket.AI_ADDRCONFIG)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_ST
