import socket
# Test socket.if_indextoname()
import _socket
if hasattr(_socket, 'if_indextoname'):
    import array
    try:
        # Array of 16 bytes
        a = array.array('B', [0] * 16)
    except TypeError:
        # Array of 'c' characters
        a = array.array('c', '\0' * 16)
    # array.buffer_info() returns a (address, length) tuple
    ifname = _socket.if_indextoname(1, a.buffer_info()[0])
    if ifname:
        print('if_indextoname() =', ifname)
# Test socket.if_nameindex()
if hasattr(_socket, 'if_nameindex'):
    if_nameindex = _socket.if_nameindex()
    for i in range(len(if_nameindex)):
        # if_nameindex is a list of tuples (index, name)
        print('%d: %s' % if_nameindex[i])
# Test socket.if_nametoindex()
