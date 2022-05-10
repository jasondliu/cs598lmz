import socket
socket.if_indextoname(network_interface)

# Open socket to listen for incoming packets
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
s.bind((network_interface, 0))

# Receive packets
while True:
    packet = s.recvfrom(65565)
    packet = packet[0]
    eth_length = 14
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print('Destination MAC: ' + eth_addr(packet[0:6]) + ' Source MAC: ' + eth_addr(packet[6:12]) + ' Protocol: ' + str(eth_protocol))

    # Parse IP header
    # take first 20 characters for the ip header
    ip_header = packet[eth_length:20+eth_length]
    
    # now unpack them :)
