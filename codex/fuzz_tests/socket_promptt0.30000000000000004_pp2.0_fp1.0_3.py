import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    for i in range(100):
        try:
            socket.if_indextoname(i)
        except ValueError:
            pass
        else:
            break
    else:
        raise TestFailed("Could not find any network interfaces")

# Test socket.if_nameindex()

def test_if_nameindex():
    for i in range(100):
        try:
            socket.if_nameindex()
        except ValueError:
            pass
        else:
            break
    else:
        raise TestFailed("Could not find any network interfaces")

# Test socket.if_nametoindex()

def test_if_nametoindex():
    for i in range(100):
        try:
            socket.if_nametoindex(socket.if_indextoname(i))
        except ValueError:
            pass
        else:
            break
    else:
        raise TestFailed("Could not find any network interfaces")

# Test socket.gethostbyname_ex()

