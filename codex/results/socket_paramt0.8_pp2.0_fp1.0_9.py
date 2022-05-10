import socket
socket.if_indextoname(if_nametoindex(self.ifname))

self.addresses = []
self.addresses.append((socket.AF_INET, (socket.INADDR_ANY, 0))
self.addresses.append((socket.AF_INET6, (socket.IN6ADDR_ANY_INIT, 0, 0, 0)))
self.addresses.append((socket.AF_LINK, (socket.ETHER_ANY, 0)))

self.sock = socket.socket(family, type)
self.sock.bind(self.addresses[family]
self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, ifname)

self.sock.sendto(packet, (ifname, SOCKET_DGRAM)) # SOCKET_DGRAM works with SOL_SOCKET.SO_BINDTODEVICE
self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, ifname)

self.sock.send
