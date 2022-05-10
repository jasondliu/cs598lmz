import socket
socket.if_indextoname(3)

#%%
import socket
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostbyaddr('151.101.193.69')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname(socket.gethostname())

#%%
import socket
socket.getfqdn()

#%%
import socket
socket.getaddrinfo('www.python.org', 80)

#%%
import socket
socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP, socket
