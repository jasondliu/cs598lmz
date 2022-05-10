import socket
import sys
import time

rssi_dict = {}

server_address = ('0.0.0.0', 4000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

node_id = 2;

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data

    rssi = int(int((data.split(" ")[2]).split("=")[1]) / 1.9)

    if rssi_dict.has_key(rssi):
        rssi_dict[rssi] = rssi_dict[rssi] + 1
    else:
        rssi_dict[rssi] = 1;

    print >>sys.stderr, 'sending acknowledgement to', address


