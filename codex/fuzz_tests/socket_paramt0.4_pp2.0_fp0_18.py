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
socket.getaddrinfo('www.baidu.com',80,0,0,socket.SOL_TCP)

#%%
import socket
socket.getaddrinfo('www.baidu.com',80,0,0,socket.SOL_UDP)

#%%
import socket
socket.gethostbyname('www.baidu.com')

#%%
import socket
socket.gethostbyname_ex('www.baidu.com')

#%%
import socket
socket.gethostbyaddr('1.1.1.1')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.getnameinfo(('127.0.0.1',80),0)

#%%
import socket
socket.getnameinfo(('127.0.0.1',80),socket.NI_NUMERICHOST)


