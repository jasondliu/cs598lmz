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
socket.gethostbyname('www.python.org')

#%%
import socket
socket.gethostbyname_ex('www.python.org')

#%%
import socket
socket.gethostbyaddr('93.184.216.34')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())[2]

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())[2][0]

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())[2][1]

#%%
import socket
socket.gethostbyname_ex(socket.gethostname())[2][2]

#%%
import
