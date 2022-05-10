import socket
socket.if_indextoname(3)

#set up the socket
sock = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))

#while true listen for packets
while True:
    packet = sock.recvfrom(65536)
    #print out the packet contents
    print(packet)
