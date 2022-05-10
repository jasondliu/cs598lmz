import socket
socket.if_indextoname(3)

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
socket.gethostbyaddr('172.217.3.110')

#%%
import socket
socket.getfqdn('172.217.3.110')

#%%
import socket
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_CANONNAME)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_
