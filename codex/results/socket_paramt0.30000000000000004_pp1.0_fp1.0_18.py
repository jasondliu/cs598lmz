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
socket.gethostbyname('www.google.com')

#%%
import socket
socket.gethostbyname_ex('www.google.com')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyaddr('192.168.1.1')

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
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.google.com
