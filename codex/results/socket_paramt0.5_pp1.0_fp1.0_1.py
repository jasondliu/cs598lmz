import socket
socket.if_indextoname(2)

#%%
import socket
socket.gethostbyname('www.google.com')

#%%
import socket
socket.gethostbyname_ex('www.google.com')

#%%
import socket
socket.gethostbyaddr('216.58.217.206')

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
socket.gethostbyaddr(socket.gethostname())

#%%
import socket
socket.getservbyname('http')

#%%
import socket
socket.getservbyport(80)

#%%
import socket
socket.getprotobyname('tcp')

#%%
import socket
socket.getprotobynumber(6)

#%%
import socket
socket.getaddrinfo('www.google.com',80)

#%%
import socket
socket.getaddrinfo('www.google.com',
