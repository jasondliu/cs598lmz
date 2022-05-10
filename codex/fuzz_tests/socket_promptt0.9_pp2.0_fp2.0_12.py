import socket
# Test socket.if_indextoname 
if_indextoname= getattr(socket,'if_indextoname',None)
if if_indextoname:
    # Test all interfaces that have been discovered on this machine
    for i in list(socket.if_nametoindex.values()):
        try:
            if_indextoname(i)
        except ValueError:
            # We could get a ValueError if the interface does not
            # exist anymore
            pass

# Test socket.getnameinfo
ni_flags=0
ni_flags |= socket.NI_NOFQDN
ni_flags |= socket.NI_NUMERICHOST
ni_flags |= socket.NI_NAMEREQD
ni_flags |= socket.NI_NUMERICSERV
ni_flags |= socket.NI_DGRAM
if hasattr(socket,'NI_WITHSCOPEID'):
    ni_flags |= socket.NI_WITHSCOPEID
#test all addrinfos
for res in socket.getaddrinfo('localhost', None):
    af, socktype, proto, canon
