import socket
# Test socket.if_indextoname()

def test_if_indextoname():
    """
    Test socket.if_indextoname()
    """
    # Get the list of network interfaces
    interfaces = socket.if_nameindex()
    for interface in interfaces:
        # Get the interface name
        interface_name = socket.if_indextoname(interface[0])
        # Check if the interface name is valid
        if interface_name is not None:
            print("Interface name: %s" % interface_name)
        else:
            print("Invalid interface name")

if __name__ == '__main__':
    test_if_indextoname()
