import socket
# Test socket.if_indextoname()

def test_if_indextoname(family, index):
    try:
        name = socket.if_indextoname(index)
    except OSError:
        return
    if name:
        addr = socket.if_nameindex()
        for if_index, if_name in addr:
            if if_name == name:
                break
        else:
            print("if_indextoname() returned '%s' for index %d, "
                  "but if_nameindex() doesn't know about it" %
                  (name, index))

# Test socket.if_indextoname() for IPv4 and IPv6

for index in range(0, 256):
    test_if_indextoname(socket.AF_INET, index)
    test_if_indextoname(socket.AF_INET6, index)
