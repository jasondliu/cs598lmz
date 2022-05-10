import socket
socket.if_indextoname(socket.if_nametoindex('en0'))

socket.if_indextoname(socket.if_nametoindex('lo0'))

try:
    socket.if_indextoname(socket.if_nametoindex('lo'))
except socket.error as err:
    print(err)

import pcapy
devs = pcapy.findalldevs()
print(devs)

mydev = devs[1]
mydev

p = pcapy.open_live(mydev, 65536, 1, 0)

dir(p)

p.fileno()

p.datalink()

p.setfilter('tcp')

p.stats()

import os

def convert_timestamp(time_stamp):
    return time.ctime(time_stamp)

def print_packet_info(packet_info):
    header, payload = packet_info
    print('Timestamp:        {}'.format(convert_timestamp(header.timestamp)))
