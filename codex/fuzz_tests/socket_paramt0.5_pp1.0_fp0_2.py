import socket
socket.if_indextoname('2')

#%%
import socket
socket.if_nametoindex('eth0')

#%%
import socket
socket.gethostbyname('www.google.com')

#%%
import socket
socket.gethostbyaddr('216.58.214.227')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname_ex('www.google.com')

#%%
import socket
socket.getfqdn('www.google.com')

#%%
import socket
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM, 0)

#%%

