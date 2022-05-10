import socket
socket.if_indextoname(2)

#%%
import socket
socket.gethostbyaddr('127.0.0.1')

#%%
import socket
socket.gethostbyname('localhost')

#%%
import socket
socket.gethostbyname_ex('localhost')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())

#%%
import socket
socket.getprotobyname('tcp')

#%%
import socket
socket.getservbyname('ftp', 'tcp')

#%%
import socket
socket.getservbyport(21, 'tcp')

#%%
import socket
socket.getaddrinfo('www.baidu.com', 80)

#%%
import socket
socket.getaddrinfo('www.baidu.com', 80, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
