import socket
socket.if_indextoname(3)

#%%
import socket
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')[2]

#%%
import socket
socket.gethostbyaddr('216.58.193.78')

#%%
import socket
socket.getnameinfo(('216.58.193.78', 80), 0)

#%%
import socket
socket.getnameinfo(('216.58.193.78', 80), 0)

#%%
import socket
socket.getnameinfo(('216.58.193.78', 80), socket.NI_NUMERICHOST)

#%%
import socket
socket.getnameinfo(('216.58.193.78', 80), socket.NI_NUMERICSERV)

#%%
import socket
socket.getnameinfo(('216.58.193.78', 80), socket.NI_NOFQDN)

#
