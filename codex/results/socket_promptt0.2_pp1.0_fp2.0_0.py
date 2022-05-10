import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    if_indextoname = socket.if_indextoname
    if_indextoname(1)
    if_indextoname(1, True)
    if_indextoname(1, False)
    if_indextoname(1, True, True)
    if_indextoname(1, True, False)
    if_indextoname(1, False, True)
    if_indextoname(1, False, False)
    if_indextoname(1, False, False, True)
    if_indextoname(1, False, False, False)
    if_indextoname(1, False, False, False, True)
    if_indextoname(1, False, False, False, False)
    if_indextoname(1, False, False, False, False, True)
    if_indextoname(1, False, False, False, False, False)
    if_indextoname(1, False, False
