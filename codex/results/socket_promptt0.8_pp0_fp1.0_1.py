import socket
# Test socket.if_indextoname()
# Equivalent to 'ip a' in shell.
if_indextoname = socket.if_indextoname
if_indextoname(1)
if_indextoname(100000000000)
try:
    if_indextoname(None)
except TypeError as e:
    print('Expected', e)

# Test socket.if_nametoindex()
# Equivalent to 'ip a' in shell.
if_nametoindex = socket.if_nametoindex
if_nametoindex('lo')
if_nametoindex('lo123')
# These work on Linux, but not macOS.
#if_nametoindex('lo0')
#if_nametoindex('lo0:0')
#if_nametoindex('lo0:1')
#if_nametoindex('lo0:2')
try:
    if_nametoindex(None)
except TypeError as e:
    print('Expected', e)

# Test socket.getaddrinfo()
# Equivalent to 'getaddrinfo' in shell.
getaddrinfo
