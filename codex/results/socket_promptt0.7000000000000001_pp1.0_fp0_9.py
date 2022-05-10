import socket
# Test socket.if_indextoname() on a socket that was bound to an interface.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(( '127.0.0.1', 20000))
if_name = socket.if_indextoname(socket.if_nametoindex('lo'))
if if_name != 'lo':
    print 'if_indextoname(if_nametoindex(\'lo\')) ==', if_name, '!= lo'
    sys.exit(1)
