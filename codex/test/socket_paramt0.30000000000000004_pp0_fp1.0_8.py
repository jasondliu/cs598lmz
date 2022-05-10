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
socket.gethostbyaddr('172.217.3.174')

#%%
import socket
socket.getservbyport(80)

#%%
import socket
socket.getservbyname('http')

#%%
import socket
socket.getprotobyname('tcp')

#%%
import socket
socket.getprotobyname('udp')

#%%
import socket
socket.getprotobyname('icmp')

#%%
import socket
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_UDP)

#
