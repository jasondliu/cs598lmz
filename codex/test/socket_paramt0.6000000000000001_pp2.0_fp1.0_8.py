import socket
socket.if_indextoname(10)

#%%
import socket
socket.gethostbyaddr("10.0.0.1")

#%%
import socket
socket.gethostbyname("localhost")

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname_ex("localhost")

#%%
import socket
socket.getnameinfo(("10.0.0.1",80),0)

#%%
import socket
socket.getprotobyname("tcp")

#%%
import socket
socket.getservbyname("ssh")

#%%
import socket
socket.getservbyport(80)

#%%
import socket
socket.getaddrinfo("www.python.org","http")

#%%
import socket
socket.getaddrinfo("www.python.org","http",0,socket.SOCK_STREAM,0,socket.AI_PASSIVE)

#%%
import socket
