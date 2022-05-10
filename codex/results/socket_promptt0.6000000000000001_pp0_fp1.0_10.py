import socket
# Test socket.if_indextoname() and socket.if_nameindex()

if_indextoname = socket.if_indextoname
if_nameindex = socket.if_nameindex

def if_nameindex_test():
    if_nameindex = socket.if_nameindex
    n = if_nameindex()
    print(n)
    assert type(n) is list
    for i in n:
        assert type(i) is tuple
        assert len(i) == 2
        assert type(i[0]) is int
        assert type(i[1]) is str

def if_indextoname_test():
    if_indextoname = socket.if_indextoname
    n = if_nameindex()
    print(n)
    for i in n:
        assert type(i[1]) is str
        assert if_indextoname(i[0]) == i[1]

if_nameindex_test()
if_indextoname_test()
