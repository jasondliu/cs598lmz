import socket
socket.if_indextoname(2)

# Go through the NIC descriptions and find the one that isn't the loopback interface
for i, desc in enumerate(socket.if_nameindex()):
    if 'lo' not in desc:
        print(desc)

# Set the last parameter to True to turn on promiscuous mode
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
# Receive 512 bytes at a time
print(s.recvfrom(512))

