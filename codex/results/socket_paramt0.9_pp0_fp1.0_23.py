import socket
socket.if_indextoname(1)

print [x for x in socket.if_nametoindex.__doc__.split() if x.startswith('en')]
print [x for x in socket.if_nametoindex.__code__.co_varnames if x.startswith('en')]

try:
    import ctypes
    print [x for x in ctypes.util.find_library('socket').split('/') if x.startswith('libc')]
except:
    pass

try:
    import lxml
    print lxml.__path__
except:
    pass

try:
    import psycopg2
    #print [x for x in psycopg2.__path__]
except:
    pass
        
try:
    import zlib
    print zlib.__file__
except:
    pass

try:
    import bz2
    print bz2.__file__
except:
    pass

try:
    import hashlib
    print hashlib.__file__
except:
    pass

try:
