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
socket.gethostbyaddr('216.58.201.46')

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
socket.getprotobyname('udp')

#%%
import socket
socket.getprotobyname('icmp')

#%%
import socket
socket.getprotobynumber(6)

#%%
import socket
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
