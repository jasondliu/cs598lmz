import socket
socket.if_indextoname(1)

#%%
import socket
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostbyaddr('216.58.192.142')

#%%
import socket
socket.getnameinfo(('216.58.192.142', 80), 0)

#%%
import socket
socket.getnameinfo(('216.58.192.142', 80), socket.NI_NUMERICHOST)

#%%
import socket
socket.getnameinfo(('216.58.192.142', 80), socket.NI_NUMERICSERV)

#%%
import socket
socket.getnameinfo(('216.58.192.142', 80), socket.NI_NOFQDN)

#%%
import socket
socket.getnameinfo(('216.58.192.142', 80), socket.NI_NAMEREQD)

#%%
import socket
