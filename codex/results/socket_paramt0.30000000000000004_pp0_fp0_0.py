import socket
socket.if_indextoname(1)

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
socket.gethostbyaddr('216.58.196.174')

#%%
import socket
socket.gethostbyname_ex('www.google.com')

#%%
import socket
socket.getfqdn('216.58.196.174')

#%%
import socket
socket.getfqdn('216.58.196.174')

#%%
import socket
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)

#
