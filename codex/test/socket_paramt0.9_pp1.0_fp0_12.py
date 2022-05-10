import socket
socket.if_indextoname(2)

# Other
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
# sock.bind(('eth0',0))
while True:
    try:
        msg, addr = sock.recvfrom(1024)
    except:
        pass
    print(msg)
