import socket
# Test socket.if_indextoname() function

def test_socket_if_indextoname(dev):
    ifname = socket.if_indextoname(0)
    if dev in ifname:
        print('function: if_indextoname() ---> PASS')
    else:
        print('function: if_indextoname() ---> FAILED')
        exit(1)

# Test socket.if_indextoname() function
def test_socket_if_indextoname_exception(dev):
    try:
        ifname = socket.if_indextoname(100)
    except ValueError:
        print('function: if_indextoname_exception() ---> PASS')
    else:
        print('function: if_indextoname_exception() ---> FAILED')
        exit(1)

# Test socket.if_nametoindex() function
def test_socket_if_nametoindex(dev):
    ifindex = socket.if_nametoindex(dev)
    if ifindex == 0:
        print('function: if
