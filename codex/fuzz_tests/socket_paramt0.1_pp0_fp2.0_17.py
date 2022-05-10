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
socket.gethostbyaddr('216.58.192.142')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.getfqdn()

#%%
import socket
socket.getaddrinfo('www.google.com', 80)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME)

#%%
import socket
socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP, socket.AI_CANONNAME, socket.AI_ADDRCONFIG)

#%%

