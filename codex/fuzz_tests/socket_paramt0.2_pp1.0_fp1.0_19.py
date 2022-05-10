import socket
socket.if_indextoname(3)

#%%
import socket
socket.if_nametoindex('eth0')

#%%
import socket
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostbyaddr('216.58.206.174')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.getfqdn()

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
socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, socket.IPPROTO_TC
