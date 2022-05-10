import socket
socket.if_indextoname(3)

#%%
import socket
socket.if_nameindex()

#%%
import socket
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostbyaddr('93.184.216.34')

#%%
import socket
socket.getnameinfo(('93.184.216.34', 80), 0)

#%%
import socket
socket.getnameinfo(('93.184.216.34', 80), socket.NI_NUMERICHOST)

#%%
import socket
socket.getnameinfo(('93.184.216.34', 80), socket.NI_NUMERICSERV)

#%%
import socket
socket.getnameinfo(('93.184.216.34', 80), socket.NI_NOFQDN)

#%%
import socket
socket.getnameinfo(('93.184.216.34', 80), socket.NI_NAMEREQD)

#%%
