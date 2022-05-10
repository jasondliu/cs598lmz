import socket
# Test socket.if_indextoname(), .if_indextoaddr() and .if_nametoindex()

def test_socket_if_nameindex():
    if_nameindex = socket.if_nameindex()
    for i in if_nameindex:
        if i[0] <= 0:
            raise TestFailed("if_nameindex returned an invalid interface index")
        if not i[1]:
            raise TestFailed("if_nameindex returned an invalid interface name")
        if not isinstance(i[1], str):
            raise TestFailed("if_nameindex returned an interface name that is not a str")
        if not socket.if_nametoindex(i[1]):
            raise TestFailed("socket.if_nametoindex(%s) failed" % repr(i[1]))

def test_socket_if_nametoindex():
    if_nameindex = socket.if_nameindex()
