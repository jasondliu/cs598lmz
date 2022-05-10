import socket
socket.if_indextoname(socket.if_nametoindex('eth0')) 

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
#s = socket.socket(socket.AF_INET, sockeT.SOCK_STREAM)
s.bind(('eth0', socket.htons(0x0806)))
while True:
    print (s.recvfrom(65565))
    
    
    
    
    
    

import time
from socket import socket, AF_INET, SOCK_DGRAM
import logging

logging.basicConfig(
    format="[%(asctime)s] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

def is_valid_packet(packet):
    return (
       
