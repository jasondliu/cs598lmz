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
socket.gethostbyaddr('93.184.216.34')

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.IPPROTO_TCP)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.IPPROTO_TCP, family=socket.AF_INET)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', proto=socket.IPPROTO_TCP, family=socket.AF_INET, type=socket.SOCK_STREAM)

#%%
import socket
