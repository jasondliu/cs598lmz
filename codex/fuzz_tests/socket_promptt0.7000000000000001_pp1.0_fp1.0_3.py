import socket
# Test socket.if_indextoname()

def test(family, addr):
    # XXX: If you get 'not available' here, please let me know
    # XXX: what platform you're on as this should be supported
    # XXX: everywhere.
    try:
        socket.if_indextoname(1)
    except socket.error:
        print("socket.if_indextoname() not available on this platform")
        return

    try:
        print(family, socket.if_indextoname(family, addr))
    except (IndexError,ValueError):
        print("invalid family or addr")

test(socket.AF_INET, b'\x00\x00\x00\x00')
test(socket.AF_INET6, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Test socket.if_nameindex()

try:
    # XXX: If you get 'not available' here
