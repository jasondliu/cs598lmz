import socket
import sys
import hashlib
import os
import time
import threading
import platform
import struct


host=''


if sys.argv[1]:
    try:
        port = int(sys.argv[1])
    except:
        print('Port invalid')
        sys.exit()
else:
    port=5002

print('Port: %s' % port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = (host,port)
sock.bind(server_address)

packet_size = 1024
packet_count = 1

# There exists a packet size limit of 512 on some older operating systems and you might get an error if you do not take care.

def recv_file(recv_size,file_size,filename):
    with open(filename,'wb') as f:
        recv_data = sock.recv(recv_size)
        f.write(recv_data)
        f.close()
    print('Done receiving')

