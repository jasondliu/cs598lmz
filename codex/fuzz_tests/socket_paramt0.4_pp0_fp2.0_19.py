import socket
socket.if_indextoname(3)

#%%
import socket
socket.if_nameindex()

#%%
import socket
socket.if_nametoindex('eth0')

#%%
import socket
socket.getaddrinfo('www.baidu.com', 80, 0, 0, socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('www.baidu.com', 'http', 0, 0, socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('www.baidu.com', 'http', 0, 0, socket.SOL_TCP, socket.AI_CANONNAME)

#%%
import socket
socket.getaddrinfo('www.baidu.com', 'http', 0, 0, socket.SOL_TCP, socket.AI_CANONNAME, socket.AI_PASSIVE)

#%%
import socket
socket.getaddrinfo('www.baidu.com', 'http', 0, 0, socket.SOL_TCP, socket.AI_CANONNAME, socket.AI_
