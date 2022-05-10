import socket
socket.if_indextoname(3)

#%%
import socket
socket.if_nameindex()

#%%
import socket
socket.if_nametoindex('lo')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname('www.google.com')

#%%
import socket
socket.gethostbyname_ex('www.google.com')

#%%
import socket
socket.gethostbyaddr('216.58.193.78')

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
