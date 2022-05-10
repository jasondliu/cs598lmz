import socket
socket.if_indextoname(1)

#%%
import socket
socket.if_nametoindex('lo')

#%%
import socket
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostbyaddr('127.0.0.1')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())

#%%
import socket
socket.getfqdn()

#%%
import socket
socket.getaddrinfo('www.python.org', 80)

#%%
import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.python.org', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG)

#%%
import socket
socket
