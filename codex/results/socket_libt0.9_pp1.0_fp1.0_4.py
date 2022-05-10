import socket
import struct

'''
Simple UDP broadcaster example
'''

transport_protocol = socket.getprotobyname('udp')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, transport_protocol)
# when you set the SO_BROADCAST option to 1 and call connect() with an address of (255.255.255.255), 
# all datagrams sent with send() will be automatically broadcast to all hosts on the local subnet
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# bind address doesn't matter, all packets are broadcast
server_socket.bind(('0.0.0.0', 9999))

print('server socket created, broadcasting...')

message = b'This is a broadcast message'
server_socket.sendto(message, ('<broadcast>', 9999))

print('server socket closed')

# it works!
# but, why the address is not 255.255.255.255?
