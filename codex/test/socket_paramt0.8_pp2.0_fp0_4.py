import socket
socket.if_indextoname(6)

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
sock.bind(("enp0s3", 0))

while True:
    packet_data, address = sock.recvfrom(65565)
    print(packet_data)
    # print(packet_data)
    # print(address)
    # print(packet_data[12:14])
    # if packet_data[12:14] == "\x08\x06":
    #     print("ARP")
    # else:
    #     print("Other protocol")
    # if packet_data[12:14] == "\x08\x00":
    #     print("IP")
    #     if packet_data[23] == "\x06":
    #         print("TCP")
    #     elif packet_data[23] == "\x01":
    #         print("ICMP")
    #     elif packet_data[23] == "\x11":
    #         print("
