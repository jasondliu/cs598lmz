import socket
# Test socket.if_indextoname() method
import sys
import struct
import time
import _thread
 
# UDP_IP = "10.16.6.2"
PORT_NO = 8888
# socket.if_indextoname(3)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# Bind the socket to the port
server_address = ('', PORT_NO)
sock.bind(server_address)


def server_udp(connection):
    try:
        print(connection)
        # data = connection.recv(1024)
        connection.sendall(b'00h1')
        time.sleep(2)

    finally:
        # Clean up the connection
        connection.close()


while True:
    # Receive the data in small chunks and retransmit it
    data, address = sock.recvfrom(4096)
    # print(address)
    # print(data)
    # print('Client Address', address
