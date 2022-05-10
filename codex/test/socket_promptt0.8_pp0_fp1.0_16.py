import socket
# Test socket.if_indextoname()
import array
HOSTNAME = 'localhost'

if __name__ == '__main__':
    interfaces = {}
    print("\n".join(socket.if_nameindex()))
    for i, name in socket.if_nameindex():
        interfaces[i] = socket.if_indextoname(i)
    print(interfaces)
    print("{0} is available at {1}".format(HOSTNAME, [i for i in interfaces.values() if i]))

    import ctypes
    libc = ctypes.CDLL(None)
    ifconf = ctypes.c_int(32)
    buf = ctypes.c_buffer(ifconf.value * 32)
    ifs = ctypes.cast(buf, ctypes.POINTER(ctypes.c_char))
    result = libc.getifaddrs(ctypes.byref(ifs))
    if result:
        raise Exception('Unable to get interfaces')
    ifa = ifs
