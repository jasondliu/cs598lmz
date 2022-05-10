import socket
# Test socket.if_indextoname()

hostname = socket.gethostname()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((hostname, 54321))

print("Serving at:")
print(sock.getsockname())

while True:
    packet, address = sock.recvfrom(2048)
    if packet:
        print("---")
        print("Received %d bytes from %s" % (len(packet), address))
        print("Calling socket.if_indextoname() to retrieve interface name")
        interface_name = socket.if_indextoname(address[1])
        print("Received packet on interface %s" % interface_name)
        # socket.gethostbyaddr() would be a waste of time, since we already
        # have the peer IP address and it may be either IPv4 or IPv6
        print("Dropping the packet at %
