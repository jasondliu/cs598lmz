import socket
socket.if_indextoname(15)

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
sock.bind(("eth0", 0))
sock.send(pkt)

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
sock.bind(("eth0", 0x800))
sock.send(pkt)

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
sock.bind(("eth0", 0x0800))
sock.send(pkt)

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
sock.bind(("eth0", 0x0806))
sock.send(pkt)

