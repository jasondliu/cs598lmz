import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    for i in range(256):
        try:
            name = socket.if_indextoname(i)
        except ValueError:
            pass
        else:
            print(i, name)

test_if_indextoname()
