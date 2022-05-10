import socket
socket.if_indextoname(7)

#%%

#%%
import socket
socket.getfqdn('127.0.0.1')
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
socket.getnameinfo(('127.0.0.1', 80), 0)
#%%
import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICHOST)
#%%
import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICSERV)
#%%
import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NOFQDN)
#%%
import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NAMEREQD)
#%%
import socket
socket.get
