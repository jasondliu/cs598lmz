import socket
# Test socket.if_indextoname() and socket.if_nameindex() on Linux
# (only) to verify that they work.
if os.name == 'posix':
    socket.if_indextoname(1)
    socket.if_nameindex()

# Test issue #13184: test that the type of socket.fromfd() is the
# same as the type of the source socket.
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST, 0))
serv.listen(5)
port = serv.getsockname()[1]
csock, addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM), (HOST, port)
csock.connect(addr)
ssock = socket.fromfd(serv.fileno(), csock.family, csock.type, csock.proto)
assert ssock.family == csock.family
assert ssock.type == csock.type
assert ssock.proto == csock.proto
serv.close()
csock.close()
ss
