import socket
# Test socket.if_indextoname()

def main():
    """
    Test socket.if_indextoname()
    """

    # Find all the interfaces
    interfaces = []
    for interface in socket.if_nameindex():
        interfaces.append(interface[1])

    for interfacename in interfaces:
        index = socket.if_nametoindex(interfacename)
        print("Interface %s has index %d" % (interfacename, index))
        print("Interface %d has name %s" % (index, socket.if_indextoname(index)))

if __name__ == "__main__":
    main()
