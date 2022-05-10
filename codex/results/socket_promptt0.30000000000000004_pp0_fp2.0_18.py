import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(1)
    if_indextoname(1, 'a')
    if_indextoname(1, 'a', 'b')
    if_indextoname(1, 'a', 'b', 'c')
    if_indextoname(1, 'a', 'b', 'c', 'd')
    if_indextoname(1, 'a', 'b', 'c', 'd', 'e')
    if_indextoname(1, 'a', 'b', 'c', 'd', 'e', 'f')
    if_indextoname(1, 'a', 'b', 'c', 'd', 'e', 'f', 'g')
    if_indextoname(1, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    if_indextoname(1, 'a', 'b', '
