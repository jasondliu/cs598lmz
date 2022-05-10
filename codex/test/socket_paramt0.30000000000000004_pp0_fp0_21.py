import socket
socket.if_indextoname(2)

#%%
import socket
socket.if_nametoindex('en0')

#%%
import socket
socket.gethostbyname('www.google.com')

#%%
import socket
socket.gethostbyname_ex('www.google.com')

#%%
import socket
socket.gethostbyname_ex('www.google.com')[2]

#%%
import socket
socket.gethostbyaddr('216.58.217.206')

#%%
import socket
socket.gethostbyaddr('216.58.217.206')[0]

#%%
import socket
socket.gethostbyaddr('216.58.217.206')[2]

#%%
import socket
socket.gethostbyaddr('216.58.217.206')[2][0]

#%%
import socket
socket.gethostbyaddr('216.58.217.206')[2][1]

#%%
import socket
socket.gethostbyaddr('216.58.217.206')[2][2]

#%%

