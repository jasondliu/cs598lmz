import socket
socket.if_indextoname(2)

#%%
import socket
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyaddr('192.168.0.1')

#%%
import socket
socket.getprotobyname('tcp')

#%%
import socket
socket.getservbyname('http', 'tcp')

#%%
import socket
socket.getservbyport(80, 'tcp')

#%%
import socket
socket.getaddrinfo('www.python.org', 80)

#%%
import socket
socket.getaddrinfo('www.python.org', 80, 0, 0, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
