import socket
socket.if_indextoname(1)

#%%
import socket
socket.if_nametoindex('lo')

#%%
import socket
socket.gethostbyname('localhost')

#%%
import socket
socket.gethostbyname_ex('localhost')

#%%
import socket
socket.gethostbyname_ex('localhost')[-1]

#%%
import socket
socket.gethostbyaddr('127.0.0.1')

#%%
import socket
socket.gethostbyaddr('127.0.0.1')[-1]

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname(socket.gethostname())

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())[-1]

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())[-1][0]

#%%
import socket
socket.gethost
