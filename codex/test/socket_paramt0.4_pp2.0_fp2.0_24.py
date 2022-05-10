import socket
socket.if_indextoname(3)

#%%
import socket
socket.gethostbyaddr('127.0.0.1')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP, flags=socket.AI_CANONNAME)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP, flags=socket.AI_CANONNAME, family=socket.AF_INET6)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP, flags=socket.AI_CANONNAME, family=socket.AF_INET6, type=socket.SOCK_DGRAM)
