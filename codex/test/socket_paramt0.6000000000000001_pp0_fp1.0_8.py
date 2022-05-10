import socket
socket.if_indextoname(7)

#%%
#!/usr/bin/env python

import socket
socket.if_nametoindex('eth0')

#%%
#!/usr/bin/env python

import socket
socket.gethostname()

#%%
#!/usr/bin/env python

import socket
socket.getfqdn('127.0.0.1')

#%%
#!/usr/bin/env python

import socket
socket.gethostbyname('localhost')

#%%
#!/usr/bin/env python

import socket
socket.gethostbyname_ex('localhost')

#%%
#!/usr/bin/env python

import socket
socket.gethostbyaddr('127.0.0.1')

#%%
#!/usr/bin/env python

import socket
socket.getaddrinfo('www.google.com', 'http')

#%%
#!/usr/bin/env python

import socket
socket.getaddrinfo('www.google.com', 'http', proto = socket.IPPROTO_TCP)

