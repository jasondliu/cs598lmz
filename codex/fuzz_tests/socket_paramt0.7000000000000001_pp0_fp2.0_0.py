import socket
socket.if_indextoname(1)

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

while True:
    packet = s.recvfrom(65565)
    packet = packet[0]
    ethernet_header = packet[0:14]
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    print("Dest MAC: " + eth_header[0].hex())
    print("Source MAC: " + eth_header[1].hex())
    print("Ethernet Type: " + eth_header[2].hex())
