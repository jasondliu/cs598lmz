import socket
socket.if_indextoname(2)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('127.0.0.1', 'http', proto=socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('127.0.0.1', 80, proto=socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('127.0.0.1', 80, proto=socket.SOL_TCP, flags=socket.AI_ADDRCONFIG)

#%%
import socket
socket.getaddrinfo('127.0.0.1', 80, proto=socket.SOL_TCP, flags=socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)

#%%
import socket
