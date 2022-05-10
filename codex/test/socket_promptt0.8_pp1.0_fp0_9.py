import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

def test_if_indextoname():
    print('*** Testing if_indextoname()')
    for interface in ('lo', 'eth0', 'wlan0', 'tun0'):
        if interface in netifaces.interfaces():
            print(interface, netifaces.if_indextoname(0))

def test_if_nametoindex():
    print('*** Testing if_nametoindex()')
    for interface in ('lo', 'eth0', 'wlan0', 'tun0'):
        if interface in netifaces.interfaces():
            print(interface, netifaces.if_nametoindex(interface))

def test_if_nameindex():
    print('*** Testing if_nameindex()')
    for interface in netifaces.if_nameindex():
        print(interface)

if __name__ == '__main__':
    test_if_indextoname()
    test_if_nametoindex()
    test_if_nameindex()
