import socket
socket.if_indextoname(2)

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
socket.gethostbyaddr('216.58.207.206')

#%%
import socket
socket.gethostname()

#%%
import socket
socket.getfqdn()

#%%
import socket
socket.getaddrinfo('www.python.org', 'http')

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM)

#%%
import socket
socket.getaddrinfo('www.python.org', 'http', socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)

#%%
import socket
